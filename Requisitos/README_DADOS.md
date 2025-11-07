# Documentação das Bases de Dados - People Analytics Selbetti

## Visão Geral

Este documento descreve as bases de dados fictícias geradas para o projeto de People Analytics da Selbetti. As bases foram criadas para permitir o planejamento e desenvolvimento do modelo de visualização antes da implementação em ambiente de produção.

## Período dos Dados

- **Início**: 01/01/2022
- **Fim**: 31/12/2024
- **Duração**: 3 anos de dados históricos

## Estrutura das Tabelas

### 1. Funcionarios

Tabela principal contendo dados cadastrais de 3000 funcionários.

**Campos:**
- `ID` (INT, PK): Identificador único do funcionário
- `Nome` (NVARCHAR): Nome completo
- `Idade` (INT): Idade do funcionário
- `Setor` (NVARCHAR): Setor de atuação (Tecnologia, Vendas, Marketing, etc.)
- `Cidade` (NVARCHAR): Cidade de residência
- `CPF` (NVARCHAR, UNIQUE): CPF do funcionário (formato válido)
- `RG` (NVARCHAR): RG do funcionário
- `Formacao` (NVARCHAR): Nível de formação (Ensino Médio, Superior, Pós-graduação, etc.)
- `Tempo_Empresa_Meses` (INT): Tempo de empresa em meses
- `Data_Aniversario` (DATE): Data de aniversário
- `Funcao_Atual` (NVARCHAR): Função/cargo atual
- `Data_Admissao` (DATE): Data de admissão na empresa
- `Status` (NVARCHAR): Status atual (Ativo ou Desligado)

**Estatísticas:**
- Total de funcionários: 3000
- Aproximadamente 85% ativos, 15% desligados
- Distribuição por setores da empresa de tecnologia

### 2. Turnover

Registros de desligamentos e análise de risco de rotatividade.

**Campos:**
- `ID` (INT, PK): Identificador único do registro
- `Funcionario_ID` (INT, FK): Referência ao funcionário
- `Data_Desligamento` (DATE): Data do desligamento (NULL para registros preditivos)
- `Tipo_Turnover` (NVARCHAR): Tipo de desligamento (Voluntário ou Involuntário)
- `Area` (NVARCHAR): Área/setor do funcionário
- `Tempo_Casa_Dias` (INT): Tempo de casa em dias
- `Custo_Desligamento` (DECIMAL): Custo estimado do desligamento em R$
- `Risco_Rotatividade` (DECIMAL): Score de risco de rotatividade (0-100)

**Características:**
- Registros de desligamentos reais (funcionários com Status = 'Desligado')
- Registros preditivos de risco para funcionários ativos (30% dos ativos)
- Distribuição: ~60% voluntário, ~40% involuntário

### 3. TD (Treinamento e Desenvolvimento)

Registros de participação em treinamentos e capacitações.

**Campos:**
- `ID` (INT, PK): Identificador único do registro
- `Funcionario_ID` (INT, FK): Referência ao funcionário
- `Treinamento_ID` (INT): Identificador do treinamento
- `Nome_Treinamento` (NVARCHAR): Nome do treinamento
- `Data_Inicio` (DATE): Data de início do treinamento
- `Data_Conclusao` (DATE): Data de conclusão (NULL se não concluído)
- `Horas_Capacitacao` (DECIMAL): Total de horas de capacitação
- `Aderencia_Plano_Educacional` (DECIMAL): Percentual de aderência ao plano (0-100)
- `Avaliacao_Eficacia` (DECIMAL): Avaliação de eficácia do treinamento (0-10, NULL se não concluído)
- `Status` (NVARCHAR): Status do treinamento (Em Andamento, Concluído, Cancelado, Não Iniciado)

**Características:**
- Cada funcionário tem 0 a 8 treinamentos no período
- Distribuição: 80% concluídos, 15% em andamento, 5% cancelados
- Treinamentos incluem: Gestão de Projetos, Liderança, Tecnologias, Soft Skills, etc.

### 4. PDI (Planos de Desenvolvimento Individual)

Registros de planos de desenvolvimento individual dos funcionários.

**Campos:**
- `ID` (INT, PK): Identificador único do registro
- `Funcionario_ID` (INT, FK): Referência ao funcionário
- `PDI_ID` (INT): Identificador do PDI
- `Area` (NVARCHAR): Área/setor do funcionário
- `Lideranca` (NVARCHAR): Nome do líder responsável
- `Data_Inicio` (DATE): Data de início do PDI
- `Data_Conclusao_Planejada` (DATE): Data planejada para conclusão
- `Data_Conclusao_Real` (DATE): Data real de conclusão (NULL se não concluído)
- `Status` (NVARCHAR): Status do PDI (Em Andamento, Concluído, Cancelado, Não Iniciado)
- `Aderencia_Percentual` (DECIMAL): Percentual de aderência ao PDI (0-100)
- `Evolucao_Competencias` (DECIMAL): Score de evolução de competências (0-10)

**Características:**
- Cada funcionário tem 0 a 3 PDIs no período
- Duração: 3 a 12 meses
- Distribuição: 70% concluídos, 20% em andamento, 10% cancelados

### 5. Clima

Resultados de pesquisas de clima organizacional e NPS de liderança.

**Campos:**
- `ID` (INT, PK): Identificador único do registro
- `Funcionario_ID` (INT, FK): Referência ao funcionário
- `Data_Pesquisa` (DATE): Data da pesquisa
- `NPS_Lideranca` (INT): Net Promoter Score de liderança (0-10)
- `Resultado_Pesquisa_Clima` (DECIMAL): Resultado da pesquisa de clima (0-10)
- `Alertas_Comportamentais` (NVARCHAR): Alertas comportamentais identificados (NULL se não houver)

**Características:**
- Pesquisas realizadas semestralmente (6 pesquisas no total)
- 70% de participação em cada pesquisa
- 10% dos registros têm alertas comportamentais

### 6. Inovacao_Competencias

Mapeamento de skills, competências e performance em trilhas estratégicas.

**Campos:**
- `ID` (INT, PK): Identificador único do registro
- `Funcionario_ID` (INT, FK): Referência ao funcionário
- `Skill_ID` (INT): Identificador da skill
- `Nome_Skill` (NVARCHAR): Nome da competência/skill
- `Nivel_Competencia` (DECIMAL): Nível de competência (0-10)
- `Gap_Critico` (BIT): Indica se há gap crítico na competência
- `Performance_Trilha_Estrategica` (DECIMAL): Performance na trilha estratégica (0-10)
- `Data_Avaliacao` (DATE): Data da avaliação

**Características:**
- Cada funcionário tem 3 a 10 skills avaliadas
- Avaliações trimestrais (1 a 12 avaliações por funcionário)
- 20% das skills têm gap crítico identificado
- Skills incluem: tecnologias, metodologias, soft skills, etc.

## Relacionamentos

Todas as tabelas relacionam-se com a tabela `Funcionarios` através da chave estrangeira `Funcionario_ID`:

```
Funcionarios (1) ──< (N) Turnover
Funcionarios (1) ──< (N) TD
Funcionarios (1) ──< (N) PDI
Funcionarios (1) ──< (N) Clima
Funcionarios (1) ──< (N) Inovacao_Competencias
```

## Como Gerar os Dados

### Pré-requisitos

1. Python 3.7 ou superior
2. Bibliotecas Python: pandas e numpy

### Execução

#### Opção 1: Script Batch (Windows - Recomendado)

Execute o arquivo `executar_geracao.bat` que irá:
- Verificar se Python está instalado
- Instalar as dependências automaticamente (pandas, numpy)
- Executar o script de geração

#### Opção 2: Manual

1. Instale as dependências:
   ```bash
   pip install pandas numpy
   ```

2. Execute o script Python:
   ```bash
   python gerar_dados.py
   ```

O script irá gerar os seguintes arquivos CSV:
- `funcionarios.csv`
- `turnover.csv`
- `td.csv`
- `pdi.csv`
- `clima.csv`
- `inovacao_competencias.csv`

## Importação para Banco de Dados

### SQL Server

1. Execute o arquivo `schema.sql` para criar a estrutura das tabelas
2. Importe os arquivos CSV usando SQL Server Management Studio ou BCP:
   ```sql
   BULK INSERT Funcionarios FROM 'funcionarios.csv' WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n', FIRSTROW = 2);
   ```

### PostgreSQL

1. Adapte o `schema.sql` para sintaxe PostgreSQL (remover IDENTITY, usar SERIAL)
2. Use COPY para importar:
   ```sql
   COPY Funcionarios FROM 'funcionarios.csv' WITH (FORMAT csv, HEADER true);
   ```

## Uso no Power BI

1. Conecte-se aos arquivos CSV ou ao banco de dados
2. Estabeleça os relacionamentos entre as tabelas usando `Funcionario_ID`
3. Crie medidas e visualizações conforme os indicadores definidos no projeto

## Indicadores Disponíveis

### Turnover e Retenção
- Turnover voluntário vs. involuntário
- Turnover por área/setor
- Turnover por tempo de casa
- Custo do desligamento
- Risco de rotatividade (preditivo)

### Desenvolvimento e Aprendizagem
- Participação em treinamentos
- Horas de capacitação
- Aderência ao plano educacional
- Avaliações de eficácia

### PDIs
- Aderência aos PDIs
- Evolução de competências
- % de PDIs concluídos vs. planejados
- Indicadores por área/liderança

### Engajamento e Clima
- NPS de liderança
- Resultados de pesquisa de clima
- Alertas comportamentais

### Inovação e Competências Estratégicas
- Mapeamento de skills
- Gaps críticos
- Performance em trilhas estratégicas

## Notas Importantes

- **Dados Fictícios**: Todos os dados são fictícios e gerados aleatoriamente
- **CPFs**: Os CPFs são gerados com formato válido, mas não são números reais
- **Consistência Temporal**: Os eventos são distribuídos ao longo dos 3 anos de forma realista
- **Relacionamentos**: Todos os relacionamentos são mantidos consistentes entre as tabelas

## Suporte

Para dúvidas ou ajustes nas bases de dados, consulte o arquivo `gerar_dados.py` e modifique os parâmetros conforme necessário.

