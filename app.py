"""
Dashboard People Analytics - Selbetti
Painel Executivo de Inteligência de Pessoas
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# Configuração da página
st.set_page_config(
    page_title="People Analytics - Selbetti",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_image(image_path):
    """Converte imagem para base64"""
    import base64
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

# Carregar CSS customizado
def load_css():
    """Carrega CSS customizado com background da Selbetti"""
    css_path = os.path.join("Imagens", "Background Selbetti - G&G BI.png")
    if os.path.exists(css_path):
        bg_image = get_base64_image(css_path)
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{bg_image}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .main .block-container {{
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            padding: 2rem;
            margin-top: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .metric-card {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #FF6B35;
        }}
        h1, h2, h3 {{
            color: #1a1a1a;
        }}
        [data-testid="stMetricValue"] {{
            font-size: 2rem;
            font-weight: bold;
        }}
        </style>
        """, unsafe_allow_html=True)
    else:
        # CSS sem background se imagem não existir
        st.markdown("""
        <style>
        .main .block-container {{
            background-color: rgba(255, 255, 255, 0.98);
            border-radius: 10px;
            padding: 2rem;
            margin-top: 2rem;
        }}
        </style>
        """, unsafe_allow_html=True)

# Carregar dados
@st.cache_data
def load_data():
    """Carrega todos os dados dos CSVs"""
    data_path = "Banco Dados"
    
    funcionarios = pd.read_csv(os.path.join(data_path, "funcionarios.csv"))
    turnover = pd.read_csv(os.path.join(data_path, "turnover.csv"))
    td = pd.read_csv(os.path.join(data_path, "td.csv"))
    pdi = pd.read_csv(os.path.join(data_path, "pdi.csv"))
    clima = pd.read_csv(os.path.join(data_path, "clima.csv"))
    inovacao = pd.read_csv(os.path.join(data_path, "inovacao_competencias.csv"))
    
    # Converter datas
    funcionarios['Data_Admissao'] = pd.to_datetime(funcionarios['Data_Admissao'])
    turnover['Data_Desligamento'] = pd.to_datetime(turnover['Data_Desligamento'], errors='coerce')
    td['Data_Inicio'] = pd.to_datetime(td['Data_Inicio'], errors='coerce')
    td['Data_Conclusao'] = pd.to_datetime(td['Data_Conclusao'], errors='coerce')
    pdi['Data_Inicio'] = pd.to_datetime(pdi['Data_Inicio'], errors='coerce')
    pdi['Data_Conclusao_Planejada'] = pd.to_datetime(pdi['Data_Conclusao_Planejada'], errors='coerce')
    pdi['Data_Conclusao_Real'] = pd.to_datetime(pdi['Data_Conclusao_Real'], errors='coerce')
    clima['Data_Pesquisa'] = pd.to_datetime(clima['Data_Pesquisa'], errors='coerce')
    inovacao['Data_Avaliacao'] = pd.to_datetime(inovacao['Data_Avaliacao'], errors='coerce')
    
    return {
        'funcionarios': funcionarios,
        'turnover': turnover,
        'td': td,
        'pdi': pdi,
        'clima': clima,
        'inovacao': inovacao
    }

# Carregar CSS
load_css()

# Carregar dados
data = load_data()

# Header com logo
logo_path = os.path.join("Imagens", "Selbetti - Logo Principal.png")
if os.path.exists(logo_path):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo_path, width=300)

st.title("📊 People Analytics - Painel Executivo")
st.markdown("---")

# ============================================
# KPIs CONSOLIDADOS - PRIMEIRA TELA
# ===========================================

st.header("🎯 Indicadores Consolidados")

# Métricas principais em 4 colunas
col1, col2, col3, col4 = st.columns(4)

# KPI 1: Total de Funcionários
funcionarios_ativos = len(data['funcionarios'][data['funcionarios']['Status'] == 'Ativo'])
total_funcionarios = len(data['funcionarios'])
with col1:
    st.metric(
        label="👥 Total de Funcionários",
        value=f"{total_funcionarios:,}",
        delta=f"{funcionarios_ativos:,} ativos"
    )

# KPI 2: Taxa de Turnover
turnover_real = data['turnover'][data['turnover']['Data_Desligamento'].notna()]
turnover_voluntario = len(turnover_real[turnover_real['Tipo_Turnover'] == 'Voluntário'])
turnover_involuntario = len(turnover_real[turnover_real['Tipo_Turnover'] == 'Involuntário'])
taxa_turnover = (len(turnover_real) / total_funcionarios) * 100 if total_funcionarios > 0 else 0

with col2:
    st.metric(
        label="🔄 Taxa de Turnover",
        value=f"{taxa_turnover:.1f}%",
        delta=f"{turnover_voluntario} voluntários"
    )

# KPI 3: Custo Total de Desligamentos
custo_total = turnover_real['Custo_Desligamento'].sum()
with col3:
    st.metric(
        label="💰 Custo de Desligamentos",
        value=f"R$ {custo_total:,.0f}",
        delta=f"{len(turnover_real)} desligamentos"
    )

# KPI 4: Risco Médio de Rotatividade
risco_medio = data['turnover']['Risco_Rotatividade'].mean()
with col4:
    st.metric(
        label="⚠️ Risco Médio de Rotatividade",
        value=f"{risco_medio:.1f}",
        delta="Score 0-100"
    )

st.markdown("---")

# Segunda linha de KPIs
col5, col6, col7, col8 = st.columns(4)

# KPI 5: Treinamentos
td_concluidos = len(data['td'][data['td']['Status'] == 'Concluído'])
total_treinamentos = len(data['td'])
horas_totais = data['td']['Horas_Capacitacao'].sum()
with col5:
    st.metric(
        label="📚 Treinamentos",
        value=f"{td_concluidos:,} concluídos",
        delta=f"{horas_totais:,.0f} horas"
    )

# KPI 6: PDIs
pdi_concluidos = len(data['pdi'][data['pdi']['Status'] == 'Concluído'])
pdi_andamento = len(data['pdi'][data['pdi']['Status'] == 'Em Andamento'])
taxa_conclusao_pdi = (pdi_concluidos / len(data['pdi'])) * 100 if len(data['pdi']) > 0 else 0
with col6:
    st.metric(
        label="🎯 PDIs",
        value=f"{taxa_conclusao_pdi:.1f}% concluídos",
        delta=f"{pdi_andamento} em andamento"
    )

# KPI 7: Clima Organizacional
clima_medio = data['clima']['Resultado_Pesquisa_Clima'].mean()
nps_medio = data['clima']['NPS_Lideranca'].mean()
with col7:
    st.metric(
        label="😊 Clima Organizacional",
        value=f"{clima_medio:.1f}/10",
        delta=f"NPS: {nps_medio:.1f}"
    )

# KPI 8: Competências
gaps_criticos = len(data['inovacao'][(data['inovacao']['Gap_Critico'] == True) | (data['inovacao']['Gap_Critico'] == 'True')])
total_skills = len(data['inovacao'])
nivel_medio_competencia = data['inovacao']['Nivel_Competencia'].mean()
with col8:
    st.metric(
        label="💡 Competências",
        value=f"{nivel_medio_competencia:.1f}/10",
        delta=f"{gaps_criticos} gaps críticos"
    )

st.markdown("---")

# ============================================
# VISUALIZAÇÕES CONSOLIDADAS
# ===========================================

st.header("📈 Visão Geral por Módulo")

# Gráficos em 2 colunas
col_left, col_right = st.columns(2)

with col_left:
    # Gráfico 1: Turnover por Tipo
    st.subheader("🔄 Turnover por Tipo")
    turnover_tipo = turnover_real.groupby('Tipo_Turnover').size().reset_index(name='Quantidade')
    fig_turnover = px.pie(
        turnover_tipo,
        values='Quantidade',
        names='Tipo_Turnover',
        color_discrete_map={'Voluntário': '#FF6B35', 'Involuntário': '#004E89'}
    )
    fig_turnover.update_layout(showlegend=True, height=300)
    st.plotly_chart(fig_turnover, use_container_width=True)
    
    # Gráfico 2: Status dos PDIs
    st.subheader("🎯 Status dos PDIs")
    pdi_status = data['pdi'].groupby('Status').size().reset_index(name='Quantidade')
    fig_pdi = px.bar(
        pdi_status,
        x='Status',
        y='Quantidade',
        color='Status',
        color_discrete_sequence=['#FF6B35', '#004E89', '#FFA500', '#808080']
    )
    fig_pdi.update_layout(showlegend=False, height=300)
    st.plotly_chart(fig_pdi, use_container_width=True)

with col_right:
    # Gráfico 3: Treinamentos por Status
    st.subheader("📚 Treinamentos por Status")
    td_status = data['td'].groupby('Status').size().reset_index(name='Quantidade')
    fig_td = px.bar(
        td_status,
        x='Status',
        y='Quantidade',
        color='Status',
        color_discrete_sequence=['#00C853', '#FF6B35', '#FFA500', '#808080']
    )
    fig_td.update_layout(showlegend=False, height=300)
    st.plotly_chart(fig_td, use_container_width=True)
    
    # Gráfico 4: Evolução do Clima
    st.subheader("😊 Evolução do Clima")
    clima_copy = data['clima'].copy()
    clima_copy['Data_Pesquisa'] = pd.to_datetime(clima_copy['Data_Pesquisa'], errors='coerce')
    clima_copy = clima_copy[clima_copy['Data_Pesquisa'].notna()]
    clima_copy['Mes'] = clima_copy['Data_Pesquisa'].dt.to_period('M').astype(str)
    clima_evolucao = clima_copy.groupby('Mes')['Resultado_Pesquisa_Clima'].mean().reset_index()
    clima_evolucao = clima_evolucao.sort_values('Mes')
    fig_clima = px.line(
        clima_evolucao,
        x='Mes',
        y='Resultado_Pesquisa_Clima',
        markers=True,
        color_discrete_sequence=['#FF6B35']
    )
    fig_clima.update_layout(showlegend=False, height=300, xaxis_title="Período", yaxis_title="Score Clima")
    st.plotly_chart(fig_clima, use_container_width=True)

# Gráfico 5: Distribuição de Funcionários por Setor
st.subheader("👥 Distribuição de Funcionários por Setor")
funcionarios_setor = data['funcionarios'][data['funcionarios']['Status'] == 'Ativo'].groupby('Setor').size().reset_index(name='Quantidade')
funcionarios_setor = funcionarios_setor.sort_values('Quantidade', ascending=False)
fig_setor = px.bar(
    funcionarios_setor,
    x='Setor',
    y='Quantidade',
    color='Quantidade',
    color_continuous_scale='Oranges'
)
fig_setor.update_layout(showlegend=False, height=400)
st.plotly_chart(fig_setor, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; padding: 1rem;'>"
    "People Analytics Selbetti | Gente & Gestão | © 2024"
    "</div>",
    unsafe_allow_html=True
)

