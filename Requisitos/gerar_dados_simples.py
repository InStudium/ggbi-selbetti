"""
Script para geração de bases de dados fictícias para People Analytics - Selbetti
Versão sem dependências externas (usa apenas bibliotecas padrão do Python)
Gera dados para 3000 funcionários com histórico de 3 anos (2022-2024)
"""

import csv
import random
from datetime import datetime, timedelta

# Seed para reprodução dos mesmos resultados
random.seed(42)

# Configurações da base
NUM_EMPLOYEES = 3000
DATA_INICIO = datetime(2022, 1, 1)
DATA_FIM = datetime(2024, 12, 31)

# Dados de referência
CITIES = ["São Paulo", "Curitiba", "Florianópolis", "Joinville", "Porto Alegre", 
          "Belo Horizonte", "Rio de Janeiro", "Brasília", "Salvador", "Recife",
          "Fortaleza", "Manaus", "Belém", "Goiânia", "Vitória", "Natal"]

DEPARTMENTS = ["Tecnologia", "Comercial", "Suporte", "Financeiro", "Gente & Gestão", 
               "Operações", "Inovação", "Marketing", "Vendas", "Atendimento", 
               "Produto", "Qualidade"]

EDUCATIONS = ["Ensino Médio", "Tecnólogo", "Graduação", "Pós-graduação", "MBA", "Mestrado", "Doutorado"]

ROLES_BY_DEPT = {
    "Tecnologia": ["Desenvolvedor", "Arquiteto", "Tech Lead", "DevOps", "QA Engineer", "Analista de Sistemas"],
    "Comercial": ["Vendedor", "Executivo de Contas", "Gerente Comercial", "Analista Comercial"],
    "Suporte": ["Analista de Suporte", "Técnico de Suporte", "Coordenador de Suporte"],
    "Financeiro": ["Analista Financeiro", "Contador", "Controller", "Gerente Financeiro"],
    "Gente & Gestão": ["Analista de RH", "Recrutador", "Gerente de RH", "Especialista em Folha"],
    "Operações": ["Analista de Operações", "Coordenador Operacional", "Supervisor", "Gerente de Operações"],
    "Inovação": ["Analista de Inovação", "Product Manager", "Innovation Lead"],
    "Marketing": ["Analista de Marketing", "Especialista em SEO", "Gerente de Marketing"],
    "Vendas": ["Vendedor", "Gerente de Vendas", "Coordenador de Vendas"],
    "Atendimento": ["Atendente", "Analista de Atendimento", "Supervisor de Atendimento"],
    "Produto": ["Product Manager", "Product Owner", "Analista de Produto"],
    "Qualidade": ["Analista de Qualidade", "Coordenador de Qualidade", "Auditor"]
}

TREINAMENTOS = [
    "Gestão de Projetos", "Liderança e Gestão de Pessoas", "Agile/Scrum",
    "Python Avançado", "JavaScript Moderno", "Cloud Computing AWS",
    "Data Analytics", "Power BI", "Comunicação Eficaz", "Vendas Consultivas",
    "Customer Success", "Design Thinking", "Product Management",
    "DevOps e CI/CD", "Segurança da Informação", "Machine Learning",
    "Negociação", "Oratória", "Excel Avançado", "Gestão de Tempo"
]

SKILLS = [
    "Python", "JavaScript", "Java", "C#", "SQL", "React", "Angular", "Vue.js",
    "Node.js", "AWS", "Azure", "Docker", "Kubernetes", "Git", "Agile", "Scrum",
    "Power BI", "Tableau", "Excel Avançado", "Gestão de Projetos", "Liderança",
    "Comunicação", "Negociação", "Vendas", "Marketing Digital", "SEO", "Design",
    "Product Management", "Data Analytics", "Machine Learning", "DevOps"
]

# Função para gerar CPF válido
def gerar_cpf():
    """Gera um CPF válido (apenas formato, não valida com Receita Federal)"""
    cpf = [random.randint(0, 9) for _ in range(9)]
    
    # Calcula primeiro dígito verificador
    soma = sum(cpf[i] * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0
    cpf.append(digito1)
    
    # Calcula segundo dígito verificador
    soma = sum(cpf[i] * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 >= 10:
        digito2 = 0
    cpf.append(digito2)
    
    return f"{''.join(map(str, cpf[:3]))}.{''.join(map(str, cpf[3:6]))}.{''.join(map(str, cpf[6:9]))}-{''.join(map(str, cpf[9:]))}"

# ============================================
# GERAR TABELA DE FUNCIONÁRIOS
# ============================================
print("Gerando tabela de Funcionários...")
employee_data = []
cpfs_gerados = set()

for i in range(NUM_EMPLOYEES):
    employee_id = i + 1
    
    # Garantir CPF único
    cpf = gerar_cpf()
    while cpf in cpfs_gerados:
        cpf = gerar_cpf()
    cpfs_gerados.add(cpf)
    
    # Dados básicos
    name = f"Funcionário {employee_id}"
    age = random.randint(22, 60)
    dept = random.choice(DEPARTMENTS)
    city = random.choice(CITIES)
    education = random.choice(EDUCATIONS)
    role = random.choice(ROLES_BY_DEPT[dept])
    
    # Datas
    dias_total = (DATA_FIM - DATA_INICIO).days
    dias_admissao = random.randint(0, dias_total)
    admission_date = DATA_INICIO + timedelta(days=dias_admissao)
    
    # Tempo de empresa em meses
    meses_empresa = (DATA_FIM.year - admission_date.year) * 12 + (DATA_FIM.month - admission_date.month)
    if meses_empresa < 0:
        meses_empresa = 0
    
    # Data de aniversário
    birthday = datetime(2024 - age, random.randint(1, 12), random.randint(1, 28))
    
    # Status (85% ativos, 15% desligados)
    status = "Ativo" if random.random() > 0.15 else "Desligado"
    
    # RG
    rg = f"{random.randint(1000000, 9999999)}-{random.randint(0, 9)}"
    
    employee_data.append([
        employee_id, name, age, dept, city, cpf, rg, education,
        meses_empresa, birthday.date().isoformat(), role, admission_date.date().isoformat(), status
    ])

print(f"✅ Funcionários gerados: {len(employee_data)}")
ativos = sum(1 for e in employee_data if e[12] == 'Ativo')
desligados = sum(1 for e in employee_data if e[12] == 'Desligado')
print(f"   - Ativos: {ativos}")
print(f"   - Desligados: {desligados}")

# Salvar funcionários
with open('funcionarios.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Nome', 'Idade', 'Setor', 'Cidade', 'CPF', 'RG', 'Formacao',
                     'Tempo_Empresa_Meses', 'Data_Aniversario', 'Funcao_Atual', 'Data_Admissao', 'Status'])
    writer.writerows(employee_data)

# ============================================
# GERAR TABELA DE TURNOVER
# ============================================
print("\nGerando tabela de Turnover...")
turnover_data = []
turnover_id = 1

# Desligamentos reais
desligados = [e for e in employee_data if e[12] == 'Desligado']

for func in desligados:
    data_admissao = datetime.strptime(func[11], '%Y-%m-%d')
    dias_total = (DATA_FIM - data_admissao).days
    dias_desligamento = random.randint(1, dias_total)
    data_desligamento = data_admissao + timedelta(days=dias_desligamento)
    
    tempo_casa_dias = (data_desligamento - data_admissao).days
    
    # 60% voluntário, 40% involuntário
    tipo = "Voluntário" if random.random() > 0.4 else "Involuntário"
    
    # Custo de desligamento
    salario_base = random.uniform(3000, 25000)
    custo = round(salario_base * random.uniform(0.5, 2.5), 2)
    
    # Risco de rotatividade
    risco = round(random.uniform(0, 100), 2)
    
    turnover_data.append([
        turnover_id, func[0], data_desligamento.date().isoformat(), tipo,
        func[3], tempo_casa_dias, custo, risco
    ])
    turnover_id += 1

# Registros preditivos para ativos (30% dos ativos)
ativos = [e for e in employee_data if e[12] == 'Ativo']
ativos_sample = random.sample(ativos, min(200, int(len(ativos) * 0.3)))

for func in ativos_sample:
    data_admissao = datetime.strptime(func[11], '%Y-%m-%d')
    dias_total = (DATA_FIM - data_admissao).days
    dias_avaliacao = random.randint(1, dias_total)
    data_avaliacao = data_admissao + timedelta(days=dias_avaliacao)
    
    risco = round(random.uniform(20, 85), 2)
    
    turnover_data.append([
        turnover_id, func[0], '', '',
        func[3], (data_avaliacao - data_admissao).days, 0, risco
    ])
    turnover_id += 1

print(f"✅ Turnover gerado: {len(turnover_data)} registros")

with open('turnover.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Funcionario_ID', 'Data_Desligamento', 'Tipo_Turnover',
                     'Area', 'Tempo_Casa_Dias', 'Custo_Desligamento', 'Risco_Rotatividade'])
    writer.writerows(turnover_data)

# ============================================
# GERAR TABELA T&D
# ============================================
print("\nGerando tabela de T&D...")
td_data = []
td_id = 1

for func in employee_data:
    # Cada funcionário tem 0 a 8 treinamentos
    num_treinamentos = random.randint(0, 8)
    data_admissao = datetime.strptime(func[11], '%Y-%m-%d')
    
    for _ in range(num_treinamentos):
        treinamento = random.choice(TREINAMENTOS)
        dias_total = (DATA_FIM - data_admissao).days
        dias_inicio = random.randint(0, dias_total)
        data_inicio = data_admissao + timedelta(days=dias_inicio)
        
        # 80% concluídos, 15% em andamento, 5% cancelados
        rand = random.random()
        if rand < 0.80:
            status = "Concluído"
            horas = round(random.uniform(4, 40), 2)
            dias_conclusao = random.randint(1, (DATA_FIM - data_inicio).days)
            data_conclusao = data_inicio + timedelta(days=dias_conclusao)
            avaliacao = round(random.uniform(6.0, 10.0), 2)
            aderencia = round(random.uniform(60, 100), 2)
        elif rand < 0.95:
            status = "Em Andamento"
            horas = round(random.uniform(2, 20), 2)
            data_conclusao = None
            avaliacao = None
            aderencia = round(random.uniform(0, 90), 2)
        else:
            status = "Cancelado"
            horas = round(random.uniform(1, 10), 2)
            data_conclusao = None
            avaliacao = None
            aderencia = round(random.uniform(0, 40), 2)
        
        td_data.append([
            td_id, func[0], random.randint(1, 100), treinamento,
            data_inicio.date().isoformat(),
            data_conclusao.date().isoformat() if data_conclusao else '',
            horas, aderencia, avaliacao if avaliacao else '', status
        ])
        td_id += 1

print(f"✅ T&D gerado: {len(td_data)} registros")

with open('td.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Funcionario_ID', 'Treinamento_ID', 'Nome_Treinamento',
                     'Data_Inicio', 'Data_Conclusao', 'Horas_Capacitacao',
                     'Aderencia_Plano_Educacional', 'Avaliacao_Eficacia', 'Status'])
    writer.writerows(td_data)

# ============================================
# GERAR TABELA PDI
# ============================================
print("\nGerando tabela de PDI...")
pdi_data = []
pdi_id = 1

for func in employee_data:
    # Cada funcionário tem 0 a 3 PDIs
    num_pdis = random.randint(0, 3)
    data_admissao = datetime.strptime(func[11], '%Y-%m-%d')
    
    for _ in range(num_pdis):
        dias_total = (DATA_FIM - data_admissao).days
        dias_inicio = random.randint(0, dias_total)
        data_inicio = data_admissao + timedelta(days=dias_inicio)
        
        # Duração: 3 a 12 meses
        meses_duracao = random.randint(3, 12)
        data_conclusao_planejada = data_inicio + timedelta(days=meses_duracao * 30)
        if data_conclusao_planejada > DATA_FIM:
            data_conclusao_planejada = DATA_FIM
        
        # 70% concluídos, 20% em andamento, 10% cancelados
        rand = random.random()
        if rand < 0.70:
            status = "Concluído"
            dias_conclusao = random.randint(0, (data_conclusao_planejada + timedelta(days=60) - data_inicio).days)
            data_conclusao_real = data_inicio + timedelta(days=dias_conclusao)
            if data_conclusao_real > DATA_FIM:
                data_conclusao_real = DATA_FIM
            aderencia = round(random.uniform(70, 100), 2)
            evolucao = round(random.uniform(6.0, 10.0), 2)
        elif rand < 0.90:
            status = "Em Andamento"
            data_conclusao_real = None
            aderencia = round(random.uniform(20, 80), 2)
            evolucao = round(random.uniform(4.0, 8.0), 2)
        else:
            status = "Cancelado"
            data_conclusao_real = None
            aderencia = round(random.uniform(0, 40), 2)
            evolucao = round(random.uniform(2.0, 6.0), 2)
        
        lideranca = f"Líder {random.randint(1, 50)}"
        
        pdi_data.append([
            pdi_id, func[0], random.randint(1, 500), func[3],
            lideranca, data_inicio.date().isoformat(),
            data_conclusao_planejada.date().isoformat(),
            data_conclusao_real.date().isoformat() if data_conclusao_real else '',
            status, aderencia, evolucao
        ])
        pdi_id += 1

print(f"✅ PDI gerado: {len(pdi_data)} registros")

with open('pdi.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Funcionario_ID', 'PDI_ID', 'Area', 'Lideranca',
                     'Data_Inicio', 'Data_Conclusao_Planejada', 'Data_Conclusao_Real',
                     'Status', 'Aderencia_Percentual', 'Evolucao_Competencias'])
    writer.writerows(pdi_data)

# ============================================
# GERAR TABELA CLIMA
# ============================================
print("\nGerando tabela de Clima...")
clima_data = []
clima_id = 1

# Pesquisas semestrais
datas_pesquisa = [
    datetime(2022, 6, 1), datetime(2022, 12, 1),
    datetime(2023, 6, 1), datetime(2023, 12, 1),
    datetime(2024, 6, 1), datetime(2024, 12, 1)
]

for data_pesquisa in datas_pesquisa:
    # Apenas funcionários que já estavam na empresa
    funcionarios_ativos = [e for e in employee_data 
                          if datetime.strptime(e[11], '%Y-%m-%d') <= data_pesquisa]
    
    # 70% de participação
    num_participantes = int(len(funcionarios_ativos) * 0.7)
    participantes = random.sample(funcionarios_ativos, num_participantes)
    
    for func in participantes:
        nps_lideranca = random.randint(0, 10)
        resultado_clima = round(random.uniform(5.0, 9.5), 2)
        
        # 10% têm alertas
        alertas = ''
        if random.random() < 0.10:
            alertas = random.choice([
                "Baixa participação em reuniões",
                "Isolamento da equipe",
                "Falta de comunicação",
                "Desmotivação observada",
                "Conflitos interpessoais"
            ])
        
        clima_data.append([
            clima_id, func[0], data_pesquisa.date().isoformat(),
            nps_lideranca, resultado_clima, alertas
        ])
        clima_id += 1

print(f"✅ Clima gerado: {len(clima_data)} registros")

with open('clima.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Funcionario_ID', 'Data_Pesquisa',
                     'NPS_Lideranca', 'Resultado_Pesquisa_Clima', 'Alertas_Comportamentais'])
    writer.writerows(clima_data)

# ============================================
# GERAR TABELA INOVAÇÃO E COMPETÊNCIAS
# ============================================
print("\nGerando tabela de Inovação e Competências...")
inovacao_data = []
inovacao_id = 1

for func in employee_data:
    # Cada funcionário tem 3 a 10 skills
    num_skills = random.randint(3, 10)
    skills_func = random.sample(SKILLS, min(num_skills, len(SKILLS)))
    data_admissao = datetime.strptime(func[11], '%Y-%m-%d')
    
    for skill in skills_func:
        # 1 a 12 avaliações (trimestrais)
        num_avaliacoes = random.randint(1, 12)
        
        for _ in range(num_avaliacoes):
            dias_total = (DATA_FIM - data_admissao).days
            dias_avaliacao = random.randint(0, dias_total)
            data_avaliacao = data_admissao + timedelta(days=dias_avaliacao)
            
            nivel_competencia = round(random.uniform(3.0, 10.0), 2)
            gap_critico = random.random() < 0.20
            performance = round(random.uniform(4.0, 10.0), 2)
            
            inovacao_data.append([
                inovacao_id, func[0], random.randint(1, 1000), skill,
                nivel_competencia, gap_critico, performance, data_avaliacao.date().isoformat()
            ])
            inovacao_id += 1

print(f"✅ Inovação e Competências gerado: {len(inovacao_data)} registros")

with open('inovacao_competencias.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Funcionario_ID', 'Skill_ID', 'Nome_Skill',
                     'Nivel_Competencia', 'Gap_Critico', 'Performance_Trilha_Estrategica', 'Data_Avaliacao'])
    writer.writerows(inovacao_data)

# ============================================
# RESUMO FINAL
# ============================================
print("\n" + "="*60)
print("ESTATÍSTICAS GERADAS:")
print("="*60)
print(f"Funcionários: {len(employee_data)}")
print(f"  - Ativos: {ativos}")
print(f"  - Desligados: {desligados}")
print(f"Turnover: {len(turnover_data)} registros")
print(f"T&D: {len(td_data)} registros")
print(f"PDI: {len(pdi_data)} registros")
print(f"Clima: {len(clima_data)} registros")
print(f"Inovação e Competências: {len(inovacao_data)} registros")
print("="*60)
print("\n✅ Arquivos CSV gerados com sucesso!")
print("="*60)
