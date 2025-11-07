-- Schema de Banco de Dados para People Analytics - Selbetti
-- Projeto: Inteligência de Pessoas
-- Data de Criação: 2024

-- ============================================
-- TABELA 1: FUNCIONARIOS
-- ============================================
CREATE TABLE Funcionarios (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Nome NVARCHAR(200) NOT NULL,
    Idade INT NOT NULL,
    Setor NVARCHAR(100) NOT NULL,
    Cidade NVARCHAR(100) NOT NULL,
    CPF NVARCHAR(14) UNIQUE NOT NULL,
    RG NVARCHAR(20) NOT NULL,
    Formacao NVARCHAR(200) NOT NULL,
    Tempo_Empresa_Meses INT NOT NULL,
    Data_Aniversario DATE NOT NULL,
    Funcao_Atual NVARCHAR(150) NOT NULL,
    Data_Admissao DATE NOT NULL,
    Status NVARCHAR(20) NOT NULL CHECK (Status IN ('Ativo', 'Desligado')),
    Data_Criacao DATETIME DEFAULT GETDATE()
);

-- ============================================
-- TABELA 2: TURNOVER
-- ============================================
CREATE TABLE Turnover (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Funcionario_ID INT NOT NULL,
    Data_Desligamento DATE NOT NULL,
    Tipo_Turnover NVARCHAR(20) NOT NULL CHECK (Tipo_Turnover IN ('Voluntário', 'Involuntário')),
    Area NVARCHAR(100) NOT NULL,
    Tempo_Casa_Dias INT NOT NULL,
    Custo_Desligamento DECIMAL(10,2) NOT NULL,
    Risco_Rotatividade DECIMAL(5,2) NOT NULL,
    Data_Registro DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (Funcionario_ID) REFERENCES Funcionarios(ID)
);

-- ============================================
-- TABELA 3: T&D (Treinamento e Desenvolvimento)
-- ============================================
CREATE TABLE TD (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Funcionario_ID INT NOT NULL,
    Treinamento_ID INT NOT NULL,
    Nome_Treinamento NVARCHAR(200) NOT NULL,
    Data_Inicio DATE NOT NULL,
    Data_Conclusao DATE NULL,
    Horas_Capacitacao DECIMAL(5,2) NOT NULL,
    Aderencia_Plano_Educacional DECIMAL(5,2) NOT NULL,
    Avaliacao_Eficacia DECIMAL(5,2) NULL,
    Status NVARCHAR(20) NOT NULL CHECK (Status IN ('Em Andamento', 'Concluído', 'Cancelado', 'Não Iniciado')),
    Data_Registro DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (Funcionario_ID) REFERENCES Funcionarios(ID)
);

-- ============================================
-- TABELA 4: PDI (Planos de Desenvolvimento Individual)
-- ============================================
CREATE TABLE PDI (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Funcionario_ID INT NOT NULL,
    PDI_ID INT NOT NULL,
    Area NVARCHAR(100) NOT NULL,
    Lideranca NVARCHAR(200) NOT NULL,
    Data_Inicio DATE NOT NULL,
    Data_Conclusao_Planejada DATE NOT NULL,
    Data_Conclusao_Real DATE NULL,
    Status NVARCHAR(20) NOT NULL CHECK (Status IN ('Em Andamento', 'Concluído', 'Cancelado', 'Não Iniciado')),
    Aderencia_Percentual DECIMAL(5,2) NOT NULL,
    Evolucao_Competencias DECIMAL(5,2) NOT NULL,
    Data_Registro DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (Funcionario_ID) REFERENCES Funcionarios(ID)
);

-- ============================================
-- TABELA 5: CLIMA
-- ============================================
CREATE TABLE Clima (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Funcionario_ID INT NOT NULL,
    Data_Pesquisa DATE NOT NULL,
    NPS_Lideranca INT NOT NULL CHECK (NPS_Lideranca >= 0 AND NPS_Lideranca <= 10),
    Resultado_Pesquisa_Clima DECIMAL(5,2) NOT NULL CHECK (Resultado_Pesquisa_Clima >= 0 AND Resultado_Pesquisa_Clima <= 10),
    Alertas_Comportamentais NVARCHAR(500) NULL,
    Data_Registro DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (Funcionario_ID) REFERENCES Funcionarios(ID)
);

-- ============================================
-- TABELA 6: INOVACAO_COMPETENCIAS
-- ============================================
CREATE TABLE Inovacao_Competencias (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Funcionario_ID INT NOT NULL,
    Skill_ID INT NOT NULL,
    Nome_Skill NVARCHAR(150) NOT NULL,
    Nivel_Competencia DECIMAL(5,2) NOT NULL CHECK (Nivel_Competencia >= 0 AND Nivel_Competencia <= 10),
    Gap_Critico BIT NOT NULL,
    Performance_Trilha_Estrategica DECIMAL(5,2) NOT NULL CHECK (Performance_Trilha_Estrategica >= 0 AND Performance_Trilha_Estrategica <= 10),
    Data_Avaliacao DATE NOT NULL,
    Data_Registro DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (Funcionario_ID) REFERENCES Funcionarios(ID)
);

-- ============================================
-- ÍNDICES PARA OTIMIZAÇÃO
-- ============================================
CREATE INDEX IX_Turnover_Funcionario_ID ON Turnover(Funcionario_ID);
CREATE INDEX IX_Turnover_Data_Desligamento ON Turnover(Data_Desligamento);
CREATE INDEX IX_TD_Funcionario_ID ON TD(Funcionario_ID);
CREATE INDEX IX_TD_Data_Inicio ON TD(Data_Inicio);
CREATE INDEX IX_PDI_Funcionario_ID ON PDI(Funcionario_ID);
CREATE INDEX IX_PDI_Status ON PDI(Status);
CREATE INDEX IX_Clima_Funcionario_ID ON Clima(Funcionario_ID);
CREATE INDEX IX_Clima_Data_Pesquisa ON Clima(Data_Pesquisa);
CREATE INDEX IX_Inovacao_Funcionario_ID ON Inovacao_Competencias(Funcionario_ID);
CREATE INDEX IX_Inovacao_Data_Avaliacao ON Inovacao_Competencias(Data_Avaliacao);
CREATE INDEX IX_Funcionarios_Status ON Funcionarios(Status);
CREATE INDEX IX_Funcionarios_Setor ON Funcionarios(Setor);

