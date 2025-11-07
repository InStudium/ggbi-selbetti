# Visualização HTML do Dashboard

## 📄 Arquivo: `index.html`

Este arquivo HTML permite visualizar o dashboard People Analytics localmente, sem precisar executar o Streamlit.

## 🚀 Como Usar

### Opção 1: Abrir Diretamente (Mais Simples)

1. Certifique-se de que os arquivos estão na estrutura correta:
   ```
   Proposta BI Selbetti G&G/
   ├── index.html
   ├── Banco Dados/
   │   ├── funcionarios.csv
   │   ├── turnover.csv
   │   ├── td.csv
   │   ├── pdi.csv
   │   ├── clima.csv
   │   └── inovacao_competencias.csv
   └── Imagens/
       ├── Background Selbetti - G&G BI.png
       └── Selbetti - Logo Principal.png
   ```

2. Clique duas vezes no arquivo `index.html` ou abra com seu navegador

3. O dashboard será carregado automaticamente!

### Opção 2: Servidor Local (Recomendado para CORS)

Se houver problemas de CORS ao carregar os CSVs, use um servidor local:

#### Python:
```bash
# Python 3
python -m http.server 8000

# Acesse: http://localhost:8000/index.html
```

#### Node.js:
```bash
# Instale http-server globalmente
npm install -g http-server

# Execute
http-server

# Acesse: http://localhost:8080/index.html
```

#### VS Code:
- Instale a extensão "Live Server"
- Clique com botão direito no `index.html`
- Selecione "Open with Live Server"

## ✨ Funcionalidades

O HTML replica a primeira tela do dashboard Streamlit:

- ✅ **8 KPIs Consolidados**
  - Total de Funcionários
  - Taxa de Turnover
  - Custo de Desligamentos
  - Risco de Rotatividade
  - Treinamentos
  - PDIs
  - Clima Organizacional
  - Competências

- ✅ **5 Visualizações Interativas**
  - Turnover por Tipo (Pizza)
  - Treinamentos por Status (Barras)
  - Status dos PDIs (Barras)
  - Evolução do Clima (Linha)
  - Distribuição por Setor (Barras)

- ✅ **Design Responsivo**
  - Adapta-se a diferentes tamanhos de tela
  - Layout moderno e profissional

- ✅ **Identidade Visual**
  - Background da Selbetti
  - Logo principal
  - Cores corporativas

## 🔧 Tecnologias Utilizadas

- **HTML5/CSS3**: Estrutura e estilização
- **JavaScript (Vanilla)**: Lógica e interatividade
- **Plotly.js**: Gráficos interativos (via CDN)
- **PapaParse**: Leitura de arquivos CSV (via CDN)

## ⚠️ Observações

1. **Navegadores Suportados**: Chrome, Firefox, Edge, Safari (versões recentes)

2. **CORS**: Alguns navegadores podem bloquear o carregamento de CSVs locais por segurança. Nesse caso, use um servidor local (Opção 2).

3. **Performance**: O HTML carrega todos os dados na memória. Para datasets muito grandes, considere otimizações.

4. **Offline**: Funciona offline após o primeiro carregamento (as bibliotecas são carregadas via CDN).

## 🆚 Comparação: HTML vs Streamlit

| Característica | HTML | Streamlit |
|----------------|------|-----------|
| **Visualização Rápida** | ✅ Sim | ⚠️ Requer instalação |
| **Interatividade** | ✅ Gráficos Plotly | ✅ Gráficos + Filtros |
| **Deploy** | ⚠️ Servidor web necessário | ✅ Streamlit Cloud |
| **Customização** | ✅ Total controle | ✅ CSS customizado |
| **Manutenção** | ⚠️ Mais código | ✅ Mais simples |

## 📝 Próximos Passos

Após visualizar o HTML e validar o design:

1. ✅ Ajustar cores/estilos se necessário
2. ✅ Testar no Streamlit (`streamlit run app.py`)
3. ✅ Fazer deploy em nuvem
4. ✅ Configurar domínio personalizado

---

**People Analytics Selbetti | Gente & Gestão | © 2024**

