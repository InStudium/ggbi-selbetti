# People Analytics - Selbetti

Dashboard executivo de People Analytics para visualização e análise de dados de recursos humanos.

## 📊 Sobre o Projeto

Este projeto implementa um dashboard de Business Intelligence focado em People Analytics, permitindo acompanhar, prever e direcionar decisões relacionadas a desempenho humano, produtividade e engajamento.

### Módulos Implementados

- **Turnover e Retenção**: Análise de desligamentos, custos e risco de rotatividade
- **Desenvolvimento e Aprendizagem**: Treinamentos, horas de capacitação e avaliações
- **PDIs**: Planos de Desenvolvimento Individual e evolução de competências
- **Clima Organizacional**: Pesquisas de clima e NPS de liderança
- **Inovação e Competências**: Mapeamento de skills e gaps críticos

## 🚀 Tecnologias

- **Streamlit**: Framework web para dashboards interativos
- **Python**: Linguagem de programação
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas
- **HTML/CSS/JavaScript**: Versão estática do dashboard

## 📁 Estrutura do Projeto

```
.
├── app.py                      # Dashboard principal (Streamlit)
├── index.html                  # Versão HTML estática
├── requirements.txt            # Dependências Python
├── README.md                   # Este arquivo
├── README_DASHBOARD.md         # Documentação do dashboard
├── ANALISE_TECNOLOGIAS.md       # Análise de tecnologias
├── LEIA-ME_HTML.md             # Guia do HTML
├── Banco Dados/                # Arquivos CSV com dados
│   ├── funcionarios.csv
│   ├── turnover.csv
│   ├── td.csv
│   ├── pdi.csv
│   ├── clima.csv
│   └── inovacao_competencias.csv
└── Imagens/                    # Assets visuais
    ├── Background Selbetti - G&G BI.png
    └── Selbetti - Logo Principal.png
```

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/InStudium/ggbi-selbetti.git
cd ggbi-selbetti
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o dashboard:
```bash
streamlit run app.py
```

4. Acesse no navegador: `http://localhost:8501`

## 📱 Visualização Rápida (HTML)

Para visualizar o dashboard sem instalar dependências:

1. Abra o arquivo `index.html` diretamente no navegador
2. Ou use um servidor local:
```bash
python -m http.server 8000
# Acesse: http://localhost:8000/index.html
```

## ☁️ Deploy

### Streamlit Cloud (Recomendado)

1. Acesse [streamlit.io/cloud](https://streamlit.io/cloud)
2. Conecte este repositório GitHub
3. Selecione `app.py` como arquivo principal
4. Deploy automático!

### Outras Opções

Consulte `README_DASHBOARD.md` para instruções detalhadas de deploy em:
- Heroku
- Azure App Service
- AWS EC2/Lightsail

## 📊 Dados

Os dados são fictícios e foram gerados para simular um período de 3 anos (2022-2024) com 3000 funcionários.

Para gerar novos dados, consulte a pasta `Requisitos/` e execute:
```bash
python Requisitos/gerar_dados.py
```

## 🎨 Design

O dashboard utiliza:
- Background personalizado da Selbetti
- Logo corporativo
- Cores da identidade visual (Laranja #FF6B35, Azul #004E89)
- Layout responsivo e moderno

## 📝 Documentação

- `README_DASHBOARD.md`: Guia completo do dashboard
- `ANALISE_TECNOLOGIAS.md`: Análise comparativa de tecnologias
- `LEIA-ME_HTML.md`: Guia da versão HTML

## 🤝 Contribuindo

Este é um projeto interno da Selbetti. Para contribuições, entre em contato com a equipe de Gente & Gestão.

## 📄 Licença

Projeto interno - Todos os direitos reservados.

## 👥 Equipe

**People Analytics Selbetti | Gente & Gestão**

---

**© 2024 Selbetti - Transformando dados de pessoas em inteligência para o crescimento da organização.**

