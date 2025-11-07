# Dashboard People Analytics - Selbetti

Dashboard executivo para visualização e análise de dados de People Analytics.

## 🚀 Tecnologias Utilizadas

- **Streamlit**: Framework web para dashboards interativos
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas e gráficos

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Dependências instaladas (ver `requirements.txt`)

## 🛠️ Instalação Local

1. Clone ou baixe o projeto

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o dashboard:
```bash
streamlit run app.py
```

4. Acesse no navegador: `http://localhost:8501`

## ☁️ Deploy em Nuvem

### Opção 1: Streamlit Cloud (Recomendado - Gratuito)

1. Crie uma conta em [streamlit.io](https://streamlit.io/cloud)
2. Conecte seu repositório GitHub
3. Selecione o arquivo `app.py` como ponto de entrada
4. Configure o domínio personalizado (se disponível)

**Vantagens:**
- Gratuito para projetos públicos
- Deploy automático via Git
- SSL automático
- Domínio personalizado disponível

### Opção 2: Heroku

1. Crie um arquivo `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Crie um arquivo `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
" > ~/.streamlit/config.toml
```

3. Deploy via Heroku CLI:
```bash
heroku create seu-app-name
git push heroku main
```

### Opção 3: Azure App Service

1. Crie um arquivo `startup.sh`:
```bash
pip install -r requirements.txt
streamlit run app.py --server.port=8000 --server.address=0.0.0.0
```

2. Configure no Azure Portal:
- Runtime: Python 3.9+
- Startup Command: `bash startup.sh`

### Opção 4: AWS EC2 / Lightsail

1. Instale Python e dependências no servidor
2. Configure nginx como reverse proxy
3. Use systemd para manter o serviço rodando

## 📁 Estrutura de Arquivos

```
.
├── app.py                          # Aplicação principal
├── requirements.txt                # Dependências Python
├── README_DASHBOARD.md             # Este arquivo
├── Banco Dados/                    # Arquivos CSV
│   ├── funcionarios.csv
│   ├── turnover.csv
│   ├── td.csv
│   ├── pdi.csv
│   ├── clima.csv
│   └── inovacao_competencias.csv
└── Imagens/                       # Assets visuais
    ├── Background Selbetti - G&G BI.png
    ├── Selbetti - Logo Principal.png
    └── ...
```

## 🎨 Personalização

### Alterar Background

Substitua o arquivo `Imagens/Background Selbetti - G&G BI.png` pelo seu background desejado.

### Alterar Logo

Substitua o arquivo `Imagens/Selbetti - Logo Principal.png` pelo seu logo.

### Cores

As cores principais podem ser alteradas no CSS dentro de `app.py`:
- Cor primária (laranja): `#FF6B35`
- Cor secundária (azul): `#004E89`

## 📊 Módulos do Dashboard

### Tela 1: Indicadores Consolidados (Atual)
- KPIs principais de todos os módulos
- Visualizações gerais
- Métricas estratégicas

### Próximas Telas (A implementar)
- Turnover e Retenção
- Desenvolvimento e Aprendizagem
- PDIs
- Clima Organizacional
- Inovação e Competências

## 🔒 Segurança

Para produção, considere:
- Autenticação de usuários
- Limitação de acesso por IP
- HTTPS obrigatório
- Rate limiting
- Logs de auditoria

## 📞 Suporte

Para dúvidas ou problemas, entre em contato com a equipe de Gente & Gestão.

---

**People Analytics Selbetti | Gente & Gestão | © 2024**

