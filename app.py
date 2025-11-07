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

def get_svg_icon(icon_name, size=24, color="#EF8943"):
    """Retorna ícone SVG 2D customizado baseado no nome"""
    icons = {
        "people": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M16 7C16 9.20914 14.2091 11 12 11C9.79086 11 8 9.20914 8 7C8 4.79086 9.79086 3 12 3C14.2091 3 16 4.79086 16 7Z"/>
            <path d="M12 14C8.13401 14 5 17.134 5 21H19C19 17.134 15.866 14 12 14Z"/>
        </svg>''',
        "turnover": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM13 17H11V15H13V17ZM13 13H11V7H13V13Z"/>
        </svg>''',
        "money": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM12 17.5C11.31 17.5 10.75 17.19 10.34 16.78L15.66 11.46C16.07 11.87 16.38 12.43 16.38 13.12C16.38 14.48 15.26 15.6 13.9 15.6C13.21 15.6 12.65 15.29 12.24 14.88L6.92 20.2C7.33 20.61 7.89 20.92 8.58 20.92C9.94 20.92 11.06 19.8 11.06 18.44C11.06 17.75 10.75 17.19 10.34 16.78L15.66 11.46C16.07 11.05 16.38 10.49 16.38 9.8C16.38 8.44 15.26 7.32 13.9 7.32C12.54 7.32 11.42 8.44 11.42 9.8C11.42 10.49 11.73 11.05 12.14 11.46L6.82 16.78C6.41 17.19 6.1 17.75 6.1 18.44C6.1 19.8 7.22 20.92 8.58 20.92C9.94 20.92 11.06 19.8 11.06 18.44C11.06 17.75 10.75 17.19 10.34 16.78L15.66 11.46C16.07 11.87 16.38 12.43 16.38 13.12C16.38 14.48 15.26 15.6 13.9 15.6Z"/>
        </svg>''',
        "risk": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2L2 7L12 12L22 7L12 2Z"/>
            <path d="M2 17L12 22L22 17V12L12 17L2 12V17Z"/>
        </svg>''',
        "training": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 3L1 9L12 15L21 10.09V17H23V9M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
        </svg>''',
        "pdi": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM10 17L5 12L6.41 10.59L10 14.17L17.59 6.58L19 8L10 17Z"/>
        </svg>''',
        "climate": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM13 17H11V15H13V17ZM13 13H11V7H13V13Z"/>
        </svg>''',
        "skills": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2L2 7L12 12L22 7L12 2Z"/>
            <path d="M2 17L12 22L22 17V12L12 17L2 12V17Z"/>
        </svg>''',
        "dashboard": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M3 3H21V21H3V3Z" stroke="{color}" stroke-width="2" fill="none"/>
            <path d="M9 9H15V15H9V9Z" fill="#00754A"/>
        </svg>''',
        "chart": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2Z"/>
        </svg>''',
        "insights": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2L2 7L12 12L22 7L12 2Z" fill="{color}"/>
            <path d="M2 17L12 22L22 17V12L12 17L2 12V17Z" fill="#00754A"/>
        </svg>''',
        "action": f'''<svg class="icon-svg" viewBox="0 0 24 24" fill="{color}" style="width: {size}px; height: {size}px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM10 17L5 12L6.41 10.59L10 14.17L17.59 6.58L19 8L10 17Z"/>
        </svg>'''
    }
    return icons.get(icon_name, "")

# Carregar CSS customizado
def load_css():
    """Carrega CSS customizado com background da Selbetti - Design moderno baseado no index.html"""
    # Versão do CSS para forçar reload quando houver mudanças
    CSS_VERSION = "2.0"
    
    css_path = os.path.join("Imagens", "Background Selbetti - G&G BI.png")
    if os.path.exists(css_path):
        bg_image = get_base64_image(css_path)
        st.markdown(f"""
        <style>
        /* Variáveis CSS */
        :root {{
            --primary-green-dark: #17392F;
            --primary-orange: #EF8943;
            --primary-green: #00754A;
            --light-gray: #F1F1F1;
            --medium-gray: #E0E0E0;
            --dark: #1a1a1a;
            --white: #ffffff;
            --shadow: rgba(0, 0, 0, 0.1);
            --shadow-hover: rgba(0, 0, 0, 0.15);
        }}
        
        /* Background fixo com imagem */
        .stApp {{
            background-image: url('data:image/png;base64,{bg_image}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        
        /* Container principal com backdrop blur */
        .main .block-container {{
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 3rem;
            margin-top: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
            max-width: 1600px;
        }}
        
        /* Título principal com gradiente */
        h1 {{
            color: var(--dark);
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, var(--primary-orange), var(--primary-green));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-align: center;
        }}
        
        /* Subtítulos com borda inferior */
        h2 {{
            color: var(--primary-green-dark);
            font-size: 2rem;
            font-weight: 600;
            margin: 3rem 0 1.5rem 0;
            padding-bottom: 1rem;
            border-bottom: 3px solid var(--primary-orange);
        }}
        
        h3 {{
            color: var(--primary-green-dark);
            font-size: 1.4rem;
            font-weight: 600;
            margin: 1.5rem 0 1rem 0;
        }}
        
        /* Cards de métricas (KPIs) melhorados */
        [data-testid="stMetricContainer"] {{
            background: linear-gradient(135deg, var(--white) 0%, var(--medium-gray) 100%);
            padding: 2rem;
            border-radius: 15px;
            border-top: 4px solid var(--primary-orange);
            box-shadow: 0 4px 16px var(--shadow);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        
        [data-testid="stMetricContainer"]::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--primary-orange), var(--primary-green));
        }}
        
        [data-testid="stMetricContainer"]:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 24px var(--shadow-hover);
        }}
        
        /* Valores das métricas */
        [data-testid="stMetricValue"] {{
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary-green-dark);
            line-height: 1.2;
        }}
        
        /* Labels das métricas */
        [data-testid="stMetricLabel"] {{
            font-size: 0.95rem;
            color: var(--primary-green-dark);
            font-weight: 600;
            margin-bottom: 0.75rem;
        }}
        
        /* Deltas das métricas */
        [data-testid="stMetricDelta"] {{
            font-size: 0.9rem;
            color: var(--primary-green);
            font-weight: 500;
        }}
        
        /* Gráficos com containers melhorados */
        [data-testid="stPlotlyChart"] {{
            background: var(--white);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 16px var(--shadow);
            border: 1px solid rgba(239, 137, 67, 0.1);
            transition: all 0.3s;
        }}
        
        [data-testid="stPlotlyChart"]:hover {{
            box-shadow: 0 8px 24px var(--shadow-hover);
            transform: translateY(-2px);
        }}
        
        /* Container para gráficos */
        .chart-wrapper {{
            background: var(--white);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 16px var(--shadow);
            border: 1px solid rgba(239, 137, 67, 0.1);
            margin-bottom: 2rem;
            transition: all 0.3s;
        }}
        
        .chart-wrapper:hover {{
            box-shadow: 0 8px 24px var(--shadow-hover);
            transform: translateY(-2px);
        }}
        
        /* Dividers */
        hr {{
            height: 3px;
            background: linear-gradient(to right, transparent, var(--primary-orange), var(--primary-green), transparent);
            border: none;
            margin: 3rem 0;
            border-radius: 2px;
        }}
        
        .divider {{
            height: 3px;
            background: linear-gradient(to right, transparent, var(--primary-orange), var(--primary-green), transparent);
            margin: 3rem 0;
            border-radius: 2px;
        }}
        
        /* Expanders (insights) melhorados */
        [data-testid="stExpander"] {{
            background: var(--white);
            border: 1px solid rgba(239, 137, 67, 0.2);
            border-radius: 10px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px var(--shadow);
        }}
        
        [data-testid="stExpander"]:hover {{
            box-shadow: 0 4px 12px var(--shadow-hover);
        }}
        
        /* Botões e elementos interativos */
        .stButton > button {{
            background: linear-gradient(135deg, var(--primary-orange), #F5A66B);
            color: white;
            border: none;
            padding: 0.75rem 2rem;
            border-radius: 10px;
            font-weight: 600;
            transition: all 0.3s;
            box-shadow: 0 4px 12px rgba(239, 137, 67, 0.3);
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(239, 137, 67, 0.4);
        }}
        
        /* Footer */
        footer {{
            visibility: hidden;
        }}
        
        /* Remover padding extra do Streamlit */
        .stApp > header {{
            visibility: hidden;
        }}
        
        /* Melhorar espaçamento geral */
        .element-container {{
            margin-bottom: 1.5rem;
        }}
        
        /* Logo centralizado */
        .logo-container {{
            text-align: center;
            margin-bottom: 2rem;
            padding-bottom: 2rem;
            border-bottom: 3px solid var(--primary-orange);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        
        /* SVG Icons */
        .icon-svg {{
            width: 24px;
            height: 24px;
            display: inline-block;
            vertical-align: middle;
        }}
        </style>
        <script>
        // Forçar reload do CSS removendo cache
        console.log('CSS carregado - versão {CSS_VERSION}');
        // Limpar cache do navegador
        if ('caches' in window) {{
            caches.keys().then(function(names) {{
                for (let name of names) caches.delete(name);
            }});
        }}
        </script>
        """.format(CSS_VERSION=CSS_VERSION), unsafe_allow_html=True)
    else:
        # CSS sem background se imagem não existir
        st.markdown("""
        <style>
        :root {{
            --primary-green-dark: #17392F;
            --primary-orange: #EF8943;
            --primary-green: #00754A;
            --light-gray: #F1F1F1;
            --medium-gray: #E0E0E0;
            --dark: #1a1a1a;
            --white: #ffffff;
            --shadow: rgba(0, 0, 0, 0.1);
            --shadow-hover: rgba(0, 0, 0, 0.15);
        }}
        
        .main .block-container {{
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 3rem;
            margin-top: 2rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
            max-width: 1600px;
        }}
        
        h1 {{
            background: linear-gradient(135deg, var(--primary-orange), var(--primary-green));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-align: center;
        }}
        
        h2 {{
            color: var(--primary-green-dark);
            border-bottom: 3px solid var(--primary-orange);
            padding-bottom: 1rem;
        }}
        
        [data-testid="stMetricContainer"] {{
            background: linear-gradient(135deg, var(--white) 0%, var(--medium-gray) 100%);
            border-radius: 15px;
            border-top: 4px solid var(--primary-orange);
            box-shadow: 0 4px 16px var(--shadow);
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

# Carregar CSS primeiro (antes de qualquer conteúdo)
load_css()

# Adicionar meta tag para evitar cache do navegador
st.markdown("""
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
""", unsafe_allow_html=True)

# Carregar dados
data = load_data()

# Header com logo centralizada e título melhorado
logo_path = os.path.join("Imagens", "Selbetti - Logo Principal.png")
if os.path.exists(logo_path):
    logo_base64 = get_base64_image(logo_path)
    st.markdown(f"""
    <div class="logo-container" style="width: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <img src="data:image/png;base64,{logo_base64}" alt="Selbetti Logo" style="max-width: 350px; margin: 0 auto 1.5rem auto; filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1)); display: block;">
        <h1 style="text-align: center; margin: 0 auto;">People Analytics</h1>
        <p style="color: #666; font-size: 1.1rem; margin-top: 0.5rem; text-align: center;">Painel Executivo de Inteligência de Pessoas</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="logo-container" style="width: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <h1 style="text-align: center; margin: 0 auto;">People Analytics</h1>
        <p style="color: #666; font-size: 1.1rem; margin-top: 0.5rem; text-align: center;">Painel Executivo de Inteligência de Pessoas</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================
# KPIs CONSOLIDADOS - PRIMEIRA TELA
# ===========================================

st.markdown(f"""
<h2>
    {get_svg_icon("insights", 32, "#EF8943")}
    Indicadores Consolidados
</h2>
""", unsafe_allow_html=True)

# Métricas principais em 4 colunas
col1, col2, col3, col4 = st.columns(4)

# KPI 1: Total de Funcionários
funcionarios_ativos = len(data['funcionarios'][data['funcionarios']['Status'] == 'Ativo'])
total_funcionarios = len(data['funcionarios'])
with col1:
    st.markdown(f'{get_svg_icon("people", 20, "#EF8943")}<span style="font-weight: 600; color: #17392F;">Total de Funcionários</span>', unsafe_allow_html=True)
    st.metric(
        label="",
        value=f"{total_funcionarios:,}",
        delta=f"{funcionarios_ativos:,} ativos"
    )

# KPI 2: Taxa de Turnover
turnover_real = data['turnover'][data['turnover']['Data_Desligamento'].notna()]
turnover_voluntario = len(turnover_real[turnover_real['Tipo_Turnover'] == 'Voluntário'])
turnover_involuntario = len(turnover_real[turnover_real['Tipo_Turnover'] == 'Involuntário'])
taxa_turnover = (len(turnover_real) / total_funcionarios) * 100 if total_funcionarios > 0 else 0

with col2:
    st.markdown(f'{get_svg_icon("turnover", 20, "#EF8943")}<span style="font-weight: 600; color: #17392F;">Taxa de Turnover</span>', unsafe_allow_html=True)
    st.metric(
        label="",
        value=f"{taxa_turnover:.1f}%",
        delta=f"{turnover_voluntario} voluntários"
    )

# KPI 3: Custo Total de Desligamentos
custo_total = turnover_real['Custo_Desligamento'].sum()
with col3:
    st.markdown(f'{get_svg_icon("money", 20, "#EF8943")}<span style="font-weight: 600; color: #17392F;">Custo de Desligamentos</span>', unsafe_allow_html=True)
    st.metric(
        label="",
        value=f"R$ {custo_total:,.0f}",
        delta=f"{len(turnover_real)} desligamentos"
    )

# KPI 4: Risco Médio de Rotatividade
risco_medio = data['turnover']['Risco_Rotatividade'].mean()
with col4:
    st.markdown(f'{get_svg_icon("risk", 20, "#EF8943")}<span style="font-weight: 600; color: #17392F;">Risco Médio de Rotatividade</span>', unsafe_allow_html=True)
    st.metric(
        label="",
        value=f"{risco_medio:.1f}",
        delta="Score 0-100"
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Segunda linha de KPIs
col5, col6, col7, col8 = st.columns(4)

# KPI 5: Treinamentos
td_concluidos = len(data['td'][data['td']['Status'] == 'Concluído'])
total_treinamentos = len(data['td'])
horas_totais = data['td']['Horas_Capacitacao'].sum()
with col5:
    st.markdown(f'{get_svg_icon("training", 20, "#EF8943")}<span style="font-weight: 600; color: #17392F;">Treinamentos</span>', unsafe_allow_html=True)
    st.metric(
        label="",
        value=f"{td_concluidos:,} concluídos",
        delta=f"{horas_totais:,.0f} horas"
    )

# KPI 6: PDIs
pdi_concluidos = len(data['pdi'][data['pdi']['Status'] == 'Concluído'])
pdi_andamento = len(data['pdi'][data['pdi']['Status'] == 'Em Andamento'])
taxa_conclusao_pdi = (pdi_concluidos / len(data['pdi'])) * 100 if len(data['pdi']) > 0 else 0
with col6:
    st.markdown(f'{get_svg_icon("pdi", 20, "#EF8943")}<span style="font-weight: 600; color: #17392F;">PDIs</span>', unsafe_allow_html=True)
    st.metric(
        label="",
        value=f"{taxa_conclusao_pdi:.1f}% concluídos",
        delta=f"{pdi_andamento} em andamento"
    )

# KPI 7: Clima Organizacional
clima_medio = data['clima']['Resultado_Pesquisa_Clima'].mean()
nps_medio = data['clima']['NPS_Lideranca'].mean()
with col7:
    st.markdown(f'{get_svg_icon("climate", 20, "#EF8943")}<span style="font-weight: 600; color: #17392F;">Clima Organizacional</span>', unsafe_allow_html=True)
    st.metric(
        label="",
        value=f"{clima_medio:.1f}/10",
        delta=f"NPS: {nps_medio:.1f}"
    )

# KPI 8: Competências
gaps_criticos = len(data['inovacao'][(data['inovacao']['Gap_Critico'] == True) | (data['inovacao']['Gap_Critico'] == 'True')])
total_skills = len(data['inovacao'])
nivel_medio_competencia = data['inovacao']['Nivel_Competencia'].mean()
with col8:
    st.markdown(f'{get_svg_icon("skills", 20, "#EF8943")}<span style="font-weight: 600; color: #17392F;">Competências</span>', unsafe_allow_html=True)
    st.metric(
        label="",
        value=f"{nivel_medio_competencia:.1f}/10",
        delta=f"{gaps_criticos} gaps críticos"
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================
# VISUALIZAÇÕES CONSOLIDADAS
# ===========================================

st.markdown(f"""
<h2>
    {get_svg_icon("dashboard", 32, "#EF8943")}
    Visão Geral por Módulo
</h2>
""", unsafe_allow_html=True)

# Gráficos em 2 colunas com espaçamento lateral para reduzir largura em 10%
col_space1, col_content, col_space2 = st.columns([0.05, 0.9, 0.05])

with col_content:
    col_left, col_right = st.columns(2)

    with col_left:
        # Gráfico 1: Turnover por Tipo
        st.markdown(f"""
        <h3>
            {get_svg_icon("turnover", 24, "#EF8943")}
            Turnover por Tipo
        </h3>
        """, unsafe_allow_html=True)
        turnover_tipo = turnover_real.groupby('Tipo_Turnover').size().reset_index(name='Quantidade')
        fig_turnover = px.pie(
            turnover_tipo,
            values='Quantidade',
            names='Tipo_Turnover',
            color_discrete_map={'Voluntário': '#EF8943', 'Involuntário': '#00754A'}
        )
        fig_turnover.update_layout(showlegend=True, height=300)
        st.plotly_chart(fig_turnover, use_container_width=True)
        
        # Gráfico 2: Status dos PDIs
        st.markdown(f"""
        <h3>
            {get_svg_icon("pdi", 24, "#EF8943")}
            Status dos PDIs
        </h3>
        """, unsafe_allow_html=True)
        pdi_status = data['pdi'].groupby('Status').size().reset_index(name='Quantidade')
        fig_pdi = px.bar(
            pdi_status,
            x='Status',
            y='Quantidade',
            color='Status',
            color_discrete_sequence=['#EF8943', '#00754A', '#F5A66B', '#E0E0E0']
        )
        fig_pdi.update_layout(showlegend=False, height=300)
        st.plotly_chart(fig_pdi, use_container_width=True)

    with col_right:
        # Gráfico 3: Treinamentos por Status
        st.markdown(f"""
        <h3>
            {get_svg_icon("training", 24, "#EF8943")}
            Treinamentos por Status
        </h3>
        """, unsafe_allow_html=True)
        td_status = data['td'].groupby('Status').size().reset_index(name='Quantidade')
        fig_td = px.bar(
            td_status,
            x='Status',
            y='Quantidade',
            color='Status',
            color_discrete_sequence=['#00754A', '#EF8943', '#F5A66B', '#E0E0E0']
        )
        fig_td.update_layout(showlegend=False, height=300)
        st.plotly_chart(fig_td, use_container_width=True)
        
        # Gráfico 4: Evolução do Clima
        st.markdown(f"""
        <h3>
            {get_svg_icon("climate", 24, "#EF8943")}
            Evolução do Clima
        </h3>
        """, unsafe_allow_html=True)
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
            color_discrete_sequence=['#EF8943']
        )
        fig_clima.update_layout(showlegend=False, height=300, xaxis_title="Período", yaxis_title="Score Clima")
        st.plotly_chart(fig_clima, use_container_width=True)

# Gráfico 5: Distribuição de Funcionários por Setor (horizontal para melhor visualização)
st.markdown(f"""
<h3>
    {get_svg_icon("people", 24, "#EF8943")}
    Distribuição de Funcionários por Setor
</h3>
""", unsafe_allow_html=True)
funcionarios_setor = data['funcionarios'][data['funcionarios']['Status'] == 'Ativo'].groupby('Setor').size().reset_index(name='Quantidade')
funcionarios_setor = funcionarios_setor.sort_values('Quantidade', ascending=True)
fig_setor = px.bar(
    funcionarios_setor,
    x='Quantidade',
    y='Setor',
    orientation='h',
    color='Quantidade',
    color_continuous_scale=[[0, '#E8F5E9'], [0.5, '#4CAF50'], [1, '#00754A']],
    text='Quantidade'
)
fig_setor.update_traces(textposition='outside')
fig_setor.update_layout(showlegend=False, height=max(400, len(funcionarios_setor) * 40), yaxis_title="", xaxis_title="Quantidade de Funcionários")
st.plotly_chart(fig_setor, use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================
# INSIGHTS E PLANOS DE AÇÃO
# ============================================

# ============================================
# TOP 10 INSIGHTS
# ============================================

st.markdown(f"""
<h2>
    {get_svg_icon("insights", 32, "#EF8943")}
    Top 10 Insights Estratégicos
</h2>
""", unsafe_allow_html=True)

def gerar_insights_e_acoes(data, total_funcionarios, turnover_real, turnover_voluntario, taxa_turnover, custo_total, 
                           risco_medio, td_concluidos, pdi_concluidos, taxa_conclusao_pdi, 
                           clima_medio, nps_medio, nivel_medio_competencia, gaps_criticos):
    """Gera insights baseados nos dados analisados"""
    
    insights = []
    
    # Insight 1: Taxa de Turnover
    if taxa_turnover > 15:
        insights.append({
            'titulo': 'Taxa de Turnover Elevada',
            'descricao': f'A taxa de turnover está em {taxa_turnover:.1f}%, acima do ideal (15%). Isso indica necessidade de ações de retenção.',
            'plano_acao': [
                'Implementar programa de retenção de talentos com foco nos setores com maior rotatividade',
                'Realizar entrevistas de desligamento estruturadas para identificar causas raiz',
                'Desenvolver plano de carreira personalizado para funcionários de alto desempenho',
                'Criar programa de mentoria e desenvolvimento para reduzir turnover voluntário'
            ]
        })
    elif taxa_turnover < 5:
        insights.append({
            'titulo': 'Taxa de Turnover Baixa - Oportunidade de Renovação',
            'descricao': f'A taxa de turnover está em {taxa_turnover:.1f}%, abaixo de 5%. Considere estratégias de renovação de talentos.',
            'plano_acao': [
                'Avaliar necessidade de renovação estratégica em áreas específicas',
                'Implementar programas de desenvolvimento interno para evitar estagnação',
                'Criar oportunidades de mobilidade interna para manter engajamento',
                'Monitorar indicadores de satisfação para prevenir turnover futuro'
            ]
        })
    else:
        insights.append({
            'titulo': 'Taxa de Turnover em Nível Aceitável',
            'descricao': f'A taxa de turnover está em {taxa_turnover:.1f}%, dentro de parâmetros aceitáveis. Manter monitoramento contínuo.',
            'plano_acao': [
                'Manter programas de retenção ativos',
                'Continuar monitorando tendências mensais',
                'Focar em desenvolvimento de talentos de alto potencial',
                'Implementar pesquisas de pulso para antecipar riscos'
            ]
        })
    
    # Insight 2: Custo de Desligamentos
    custo_medio = custo_total / len(turnover_real) if len(turnover_real) > 0 else 0
    if custo_medio > 50000:
        insights.append({
            'titulo': 'Alto Custo Médio de Desligamentos',
            'descricao': f'O custo médio por desligamento é de R$ {custo_medio:,.0f}, indicando impacto financeiro significativo.',
            'plano_acao': [
                'Priorizar ações preventivas de retenção para reduzir custos futuros',
                'Implementar programas de onboarding mais eficazes para reduzir turnover inicial',
                'Desenvolver estratégias de sucessão para cargos críticos',
                'Criar métricas de ROI para programas de retenção'
            ]
        })
    
    # Insight 3: Risco de Rotatividade
    if risco_medio > 70:
        insights.append({
            'titulo': 'Alto Risco de Rotatividade Identificado',
            'descricao': f'O risco médio de rotatividade está em {risco_medio:.1f}/100, indicando necessidade de ações imediatas.',
            'plano_acao': [
                'Identificar funcionários de alto risco e criar planos de ação individualizados',
                'Implementar programas de engajamento específicos para grupos de risco',
                'Realizar pesquisas de pulso focadas em funcionários com alto risco',
                'Desenvolver estratégias de retenção proativas antes do desligamento'
            ]
        })
    
    # Insight 4: PDIs
    if taxa_conclusao_pdi < 60:
        insights.append({
            'titulo': 'Baixa Taxa de Conclusão de PDIs',
            'descricao': f'Apenas {taxa_conclusao_pdi:.1f}% dos PDIs foram concluídos, indicando necessidade de acompanhamento mais efetivo.',
            'plano_acao': [
                'Implementar sistema de acompanhamento mensal de PDIs',
                'Criar reuniões de check-in regulares entre gestores e colaboradores',
                'Desenvolver recursos e ferramentas para facilitar conclusão de PDIs',
                'Estabelecer metas claras e prazos realistas para cada PDI'
            ]
        })
    else:
        insights.append({
            'titulo': 'Boa Taxa de Conclusão de PDIs',
            'descricao': f'{taxa_conclusao_pdi:.1f}% dos PDIs foram concluídos. Manter o foco em qualidade e impacto dos desenvolvimentos.',
            'plano_acao': [
                'Avaliar o impacto real dos PDIs concluídos no desenvolvimento dos colaboradores',
                'Expandir programas de desenvolvimento para mais funcionários',
                'Criar biblioteca de recursos e melhores práticas de desenvolvimento',
                'Implementar feedback 360° para validar evolução'
            ]
        })
    
    # Insight 5: Clima Organizacional
    if clima_medio < 7:
        insights.append({
            'titulo': 'Clima Organizacional Requer Atenção',
            'descricao': f'O score de clima organizacional está em {clima_medio:.1f}/10, abaixo do ideal. Ações de melhoria são necessárias.',
            'plano_acao': [
                'Realizar grupos focais para identificar causas específicas de insatisfação',
                'Implementar ações rápidas (quick wins) para melhorar percepção imediata',
                'Desenvolver plano de comunicação mais transparente e frequente',
                'Criar programas de reconhecimento e valorização dos colaboradores'
            ]
        })
    else:
        insights.append({
            'titulo': 'Clima Organizacional Positivo',
            'descricao': f'O score de clima está em {clima_medio:.1f}/10. Manter práticas que geram engajamento e satisfação.',
            'plano_acao': [
                'Identificar e replicar práticas de sucesso em todos os setores',
                'Manter frequência de pesquisas de clima para monitoramento contínuo',
                'Desenvolver programas de employer branding baseados no clima positivo',
                'Criar canais de feedback contínuo para manter engajamento'
            ]
        })
    
    # Insight 6: NPS de Liderança
    if nps_medio < 50:
        insights.append({
            'titulo': 'NPS de Liderança Abaixo do Esperado',
            'descricao': f'O NPS de liderança está em {nps_medio:.1f}, indicando necessidade de desenvolvimento de líderes.',
            'plano_acao': [
                'Implementar programa de desenvolvimento de liderança estruturado',
                'Criar feedback 360° para identificar gaps específicos de liderança',
                'Desenvolver programa de coaching para líderes com baixo NPS',
                'Estabelecer métricas de liderança efetiva e acompanhamento regular'
            ]
        })
    
    # Insight 7: Competências e Gaps
    if gaps_criticos > 50:
        insights.append({
            'titulo': 'Alto Número de Gaps Críticos de Competências',
            'descricao': f'Foram identificados {gaps_criticos} gaps críticos de competências, requerendo ações de desenvolvimento prioritárias.',
            'plano_acao': [
                'Priorizar desenvolvimento de competências críticas identificadas',
                'Criar programas de treinamento específicos para gaps mais frequentes',
                'Implementar sistema de mentoria para transferência de conhecimento',
                'Desenvolver plano de capacitação de curto, médio e longo prazo'
            ]
        })
    
    # Insight 8: Treinamentos
    taxa_conclusao_td = (td_concluidos / len(data['td'])) * 100 if len(data['td']) > 0 else 0
    if taxa_conclusao_td < 70:
        insights.append({
            'titulo': 'Taxa de Conclusão de Treinamentos Abaixo do Ideal',
            'descricao': f'Apenas {taxa_conclusao_td:.1f}% dos treinamentos foram concluídos, indicando necessidade de melhor engajamento.',
            'plano_acao': [
                'Avaliar barreiras para conclusão de treinamentos (tempo, relevância, formato)',
                'Implementar treinamentos mais curtos e focados (microlearning)',
                'Criar sistema de gamificação para aumentar engajamento',
                'Estabelecer metas e reconhecimento para conclusão de treinamentos'
            ]
        })
    
    # Insight 9: Distribuição por Setor
    funcionarios_setor = data['funcionarios'][data['funcionarios']['Status'] == 'Ativo'].groupby('Setor').size()
    setor_maior = funcionarios_setor.idxmax()
    setor_menor = funcionarios_setor.idxmin()
    razao = funcionarios_setor.max() / funcionarios_setor.min() if funcionarios_setor.min() > 0 else 0
    
    if razao > 3:
        insights.append({
            'titulo': 'Desequilíbrio na Distribuição de Funcionários por Setor',
            'descricao': f'O setor {setor_maior} tem {funcionarios_setor.max()} funcionários, enquanto {setor_menor} tem apenas {funcionarios_setor.min()}.',
            'plano_acao': [
                'Avaliar necessidade de redistribuição ou contratações estratégicas',
                'Desenvolver planos de crescimento específicos para setores menores',
                'Criar programas de mobilidade interna entre setores',
                'Analisar impacto do desequilíbrio na eficiência organizacional'
            ]
        })
    
    # Insight 10: Turnover Voluntário vs Involuntário
    if len(turnover_real) > 0:
        pct_voluntario = (turnover_voluntario / len(turnover_real)) * 100
        if pct_voluntario > 70:
            insights.append({
                'titulo': 'Alta Proporção de Turnover Voluntário',
                'descricao': f'{pct_voluntario:.1f}% dos desligamentos são voluntários, indicando necessidade de melhorar retenção.',
                'plano_acao': [
                    'Realizar entrevistas de saída detalhadas para identificar padrões',
                    'Implementar programas de retenção específicos para causas mais frequentes',
                    'Desenvolver estratégias de compensação e benefícios competitivos',
                    'Criar programas de desenvolvimento de carreira mais atrativos'
                ]
            })
    
    # Garantir que temos pelo menos 10 insights
    while len(insights) < 10:
        insights.append({
            'titulo': 'Monitoramento Contínuo de Métricas',
            'descricao': 'Manter acompanhamento regular de todas as métricas de People Analytics para identificar tendências.',
            'plano_acao': [
                'Estabelecer dashboard de acompanhamento mensal',
                'Criar alertas automáticos para métricas fora do esperado',
                'Realizar análises comparativas trimestrais',
                'Desenvolver cultura de decisão baseada em dados'
            ]
        })
    
    return insights[:10]

# Gerar insights
insights = gerar_insights_e_acoes(
    data, total_funcionarios, turnover_real, turnover_voluntario, taxa_turnover, custo_total,
    risco_medio, td_concluidos, pdi_concluidos, taxa_conclusao_pdi,
    clima_medio, nps_medio, nivel_medio_competencia, gaps_criticos
)

# Exibir Top 10 Insights
st.markdown("""
<div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1); margin-bottom: 2rem;">
""", unsafe_allow_html=True)

for i, insight in enumerate(insights, 1):
    st.markdown(f"""
    <div style="background: {'rgba(239, 137, 67, 0.1)' if i <= 3 else 'rgba(255, 255, 255, 0.5)'}; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem; border-left: 4px solid #EF8943;">
        <h3 style="color: #17392F; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
            {get_svg_icon("insights", 24, "#EF8943")}
            Insight {i}: {insight['titulo']}
        </h3>
        <p style="color: #666; margin-bottom: 0.5rem; line-height: 1.6;">{insight['descricao']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================
# PLANO DE AÇÃO CONSOLIDADO
# ============================================

st.markdown(f"""
<h2>
    {get_svg_icon("action", 32, "#EF8943")}
    Plano de Ação Estratégico
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);">
    <p style="color: #666; margin-bottom: 1.5rem; font-size: 1.1rem; line-height: 1.6;">
        Com base nos <strong>Top 10 Insights Estratégicos</strong> identificados, apresentamos um plano de ação consolidado 
        para otimizar os resultados de People Analytics da organização.
    </p>
""", unsafe_allow_html=True)

# Consolidar todas as ações dos insights
todas_acoes = []
for i, insight in enumerate(insights, 1):
    for acao in insight['plano_acao']:
        todas_acoes.append({
            'acao': acao,
            'insight_origem': f"Insight {i}: {insight['titulo']}",
            'prioridade': 'Alta' if i <= 3 else 'Média' if i <= 6 else 'Baixa'
        })

# Agrupar ações por categoria
acoes_por_categoria = {
    'Retenção e Turnover': [],
    'Desenvolvimento e Treinamento': [],
    'Clima e Engajamento': [],
    'Liderança e Gestão': [],
    'Competências e Inovação': [],
    'Monitoramento e Análise': []
}

for acao_item in todas_acoes:
    acao = acao_item['acao'].lower()
    if any(palavra in acao for palavra in ['retenção', 'turnover', 'desligamento', 'rotatividade']):
        acoes_por_categoria['Retenção e Turnover'].append(acao_item)
    elif any(palavra in acao for palavra in ['treinamento', 'desenvolvimento', 'pdi', 'capacitação', 'mentoria']):
        acoes_por_categoria['Desenvolvimento e Treinamento'].append(acao_item)
    elif any(palavra in acao for palavra in ['clima', 'satisfação', 'engajamento', 'reconhecimento', 'comunicação']):
        acoes_por_categoria['Clima e Engajamento'].append(acao_item)
    elif any(palavra in acao for palavra in ['liderança', 'gestor', 'coaching', 'feedback 360']):
        acoes_por_categoria['Liderança e Gestão'].append(acao_item)
    elif any(palavra in acao for palavra in ['competência', 'gap', 'inovação', 'skill']):
        acoes_por_categoria['Competências e Inovação'].append(acao_item)
    else:
        acoes_por_categoria['Monitoramento e Análise'].append(acao_item)

# Exibir plano de ação por categoria
categoria_icons = {
    'Retenção e Turnover': 'turnover',
    'Desenvolvimento e Treinamento': 'training',
    'Clima e Engajamento': 'climate',
    'Liderança e Gestão': 'pdi',
    'Competências e Inovação': 'skills',
    'Monitoramento e Análise': 'dashboard'
}

for categoria, acoes in acoes_por_categoria.items():
    if acoes:
        icon_name = categoria_icons.get(categoria, 'action')
        st.markdown(f"""
        <div style="margin-bottom: 2rem;">
            <h3 style="color: #17392F; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; border-bottom: 2px solid #EF8943; padding-bottom: 0.5rem;">
                {get_svg_icon(icon_name, 28, "#EF8943")}
                {categoria}
            </h3>
            <div style="background: rgba(241, 241, 241, 0.5); padding: 1.5rem; border-radius: 10px;">
        """, unsafe_allow_html=True)
        
        for idx, acao_item in enumerate(acoes[:10], 1):  # Limitar a 10 ações por categoria
            prioridade_color = '#EF8943' if acao_item['prioridade'] == 'Alta' else '#00754A' if acao_item['prioridade'] == 'Média' else '#666'
            st.markdown(f"""
            <div style="margin-bottom: 1rem; padding: 1rem; background: white; border-radius: 8px; border-left: 4px solid {prioridade_color};">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                    <p style="color: #17392F; font-weight: 600; margin: 0; flex: 1;">{acao_item['acao']}</p>
                    <span style="background: {prioridade_color}; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem; font-weight: 600;">
                        {acao_item['prioridade']}
                    </span>
                </div>
                <p style="color: #666; font-size: 0.9rem; margin: 0; font-style: italic;">
                    Origem: {acao_item['insight_origem']}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown("""
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Footer
st.markdown(
    "<div style='text-align: center; color: #666; padding: 2rem; margin-top: 3rem; border-top: 2px solid #E0E0E0; font-size: 0.95rem;'>"
    "People Analytics Selbetti | Gente & Gestão | © 2024"
    "</div>",
    unsafe_allow_html=True
)

