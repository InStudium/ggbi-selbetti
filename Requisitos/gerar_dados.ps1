# Script PowerShell para geração de bases de dados fictícias para People Analytics - Selbetti
# Gera dados para 3000 funcionários com histórico de 3 anos (2022-2024)

# Configuração
$DATA_INICIO = Get-Date "2022-01-01"
$DATA_FIM = Get-Date "2024-12-31"
$NUM_FUNCIONARIOS = 3000

# Sementes para reprodutibilidade
$random = [System.Random]::new(42)

# Definir setores e áreas
$SETORES = @(
    'Tecnologia', 'Comercial', 'Suporte', 'Financeiro', 'Gente & Gestão', 
    'Operações', 'Inovação', 'Marketing', 'Produto', 'Qualidade', 
    'Atendimento', 'Administrativo'
)

$FUNCOES = @{
    'Tecnologia' = @('Desenvolvedor Full Stack', 'Desenvolvedor Backend', 'Desenvolvedor Frontend', 'Arquiteto de Software', 'DevOps Engineer', 'QA Engineer', 'Tech Lead')
    'Comercial' = @('Vendedor', 'Gerente de Vendas', 'Analista Comercial', 'Coordenador de Vendas', 'Diretor Comercial', 'Executivo de Contas')
    'Suporte' = @('Técnico de Suporte', 'Analista de Suporte', 'Especialista Técnico', 'Coordenador de Suporte', 'Gerente de Suporte')
    'Financeiro' = @('Analista Financeiro', 'Contador', 'Gerente Financeiro', 'Controller', 'Analista de Contas a Pagar', 'Diretor Financeiro')
    'Gente & Gestão' = @('Analista de RH', 'Gerente de RH', 'Recrutador', 'Especialista em Folha', 'Coordenador de T&D', 'Diretor de RH')
    'Operações' = @('Analista de Operações', 'Gerente de Operações', 'Coordenador Operacional', 'Supervisor de Produção', 'Diretor de Operações')
    'Inovação' = @('Analista de Inovação', 'Coordenador de Inovação', 'Gerente de Inovação', 'Especialista em Inovação', 'Diretor de Inovação')
    'Marketing' = @('Analista de Marketing', 'Gerente de Marketing', 'Especialista em SEO', 'Content Manager', 'Social Media', 'Marketing Digital')
    'Produto' = @('Product Manager', 'Product Owner', 'Analista de Produto', 'Gerente de Produto', 'Diretor de Produto')
    'Qualidade' = @('Analista de Qualidade', 'Coordenador de Qualidade', 'Gerente de Qualidade', 'Auditor de Qualidade')
    'Atendimento' = @('Atendente', 'Analista de Atendimento', 'Supervisor de Atendimento', 'Gerente de Atendimento', 'Especialista em Suporte')
    'Administrativo' = @('Assistente Administrativo', 'Analista Administrativo', 'Coordenador Administrativo', 'Gerente Administrativo')
}

$FORMACOES = @('Ensino Médio', 'Tecnólogo', 'Graduação', 'Pós-graduação', 'MBA', 'Mestrado', 'Doutorado')
$CIDADES_BR = @('São Paulo', 'Curitiba', 'Florianópolis', 'Joinville', 'Porto Alegre', 'Belo Horizonte', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Recife', 'Fortaleza', 'Manaus', 'Belém', 'Goiânia', 'Vitória', 'Natal')
$TREINAMENTOS = @('Gestão de Projetos', 'Liderança e Gestão de Pessoas', 'Agile/Scrum', 'Python Avançado', 'JavaScript Moderno', 'Cloud Computing AWS', 'Data Analytics', 'Power BI', 'Comunicação Eficaz', 'Vendas Consultivas', 'Customer Success', 'Design Thinking', 'Product Management', 'DevOps e CI/CD', 'Segurança da Informação', 'Machine Learning', 'Negociação', 'Oratória', 'Excel Avançado', 'Gestão de Tempo')
$SKILLS = @('Python', 'JavaScript', 'Java', 'C#', 'SQL', 'React', 'Angular', 'Vue.js', 'Node.js', 'AWS', 'Azure', 'Docker', 'Kubernetes', 'Git', 'Agile', 'Scrum', 'Power BI', 'Tableau', 'Excel Avançado', 'Gestão de Projetos', 'Liderança', 'Comunicação', 'Negociação', 'Vendas', 'Marketing Digital', 'SEO', 'Design', 'Product Management', 'Data Analytics', 'Machine Learning', 'DevOps')

# Função para gerar CPF
function Gerar-CPF {
    $cpf = @()
    for ($i = 0; $i -lt 9; $i++) {
        $cpf += $random.Next(0, 10)
    }
    
    # Calcular primeiro dígito
    $soma = 0
    for ($i = 0; $i -lt 9; $i++) {
        $soma += $cpf[$i] * (10 - $i)
    }
    $digito1 = 11 - ($soma % 11)
    if ($digito1 -ge 10) { $digito1 = 0 }
    $cpf += $digito1
    
    # Calcular segundo dígito
    $soma = 0
    for ($i = 0; $i -lt 10; $i++) {
        $soma += $cpf[$i] * (11 - $i)
    }
    $digito2 = 11 - ($soma % 11)
    if ($digito2 -ge 10) { $digito2 = 0 }
    $cpf += $digito2
    
    return "$($cpf[0..2] -join '')$($cpf[3..5] -join '')$($cpf[6..8] -join '')-$($cpf[9..10] -join '')"
}

# Função para gerar nome aleatório
function Gerar-Nome {
    $nomes = @('João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Juliana', 'Fernando', 'Patricia', 'Ricardo', 'Mariana', 'Roberto', 'Camila', 'Lucas', 'Beatriz', 'Rafael', 'Larissa', 'Gabriel', 'Amanda', 'Thiago', 'Bruna', 'Felipe', 'Carolina', 'André', 'Isabela', 'Rodrigo', 'Vanessa', 'Marcos', 'Renata', 'Paulo', 'Daniela')
    $sobrenomes = @('Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Costa', 'Rodrigues', 'Almeida', 'Nascimento', 'Lima', 'Araújo', 'Fernandes', 'Carvalho', 'Gomes', 'Martins', 'Rocha', 'Ribeiro', 'Alves', 'Monteiro', 'Mendes')
    return "$($nomes[$random.Next($nomes.Length)]) $($sobrenomes[$random.Next($sobrenomes.Length)]) $($sobrenomes[$random.Next($sobrenomes.Length)])"
}

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "GERAÇÃO DE BASES DE DADOS - PEOPLE ANALYTICS SELBETTI" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Período: $($DATA_INICIO.ToString('dd/MM/yyyy')) a $($DATA_FIM.ToString('dd/MM/yyyy'))"
Write-Host "Número de funcionários: $NUM_FUNCIONARIOS"
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Gerar Funcionários
Write-Host "Gerando tabela de Funcionários..." -ForegroundColor Yellow
$funcionarios = @()
$cpfsGerados = @{}

for ($i = 1; $i -le $NUM_FUNCIONARIOS; $i++) {
    $cpf = Gerar-CPF
    while ($cpfsGerados.ContainsKey($cpf)) {
        $cpf = Gerar-CPF
    }
    $cpfsGerados[$cpf] = $true
    
    $setor = $SETORES[$random.Next($SETORES.Length)]
    $funcao = $FUNCOES[$setor][$random.Next($FUNCOES[$setor].Length)]
    
    $diasTotal = ($DATA_FIM - $DATA_INICIO).Days
    $diasAdmissao = $random.Next(0, $diasTotal)
    $dataAdmissao = $DATA_INICIO.AddDays($diasAdmissao)
    
    $mesesEmpresa = [Math]::Floor(($DATA_FIM - $dataAdmissao).TotalDays / 30)
    if ($mesesEmpresa -lt 0) { $mesesEmpresa = 0 }
    
    $status = if ($random.NextDouble() -gt 0.15) { 'Ativo' } else { 'Desligado' }
    $idade = $random.Next(22, 66)
    $anoNascimento = 2024 - $idade
    $dataAniversario = Get-Date "$anoNascimento-$($random.Next(1,13))-$($random.Next(1,29))"
    
    $funcionario = [PSCustomObject]@{
        ID = $i
        Nome = Gerar-Nome
        Idade = $idade
        Setor = $setor
        Cidade = $CIDADES_BR[$random.Next($CIDADES_BR.Length)]
        CPF = $cpf
        RG = "$($random.Next(1000000, 10000000))-$($random.Next(0, 10))"
        Formacao = $FORMACOES[$random.Next($FORMACOES.Length)]
        Tempo_Empresa_Meses = $mesesEmpresa
        Data_Aniversario = $dataAniversario.ToString('yyyy-MM-dd')
        Funcao_Atual = $funcao
        Data_Admissao = $dataAdmissao.ToString('yyyy-MM-dd')
        Status = $status
    }
    $funcionarios += $funcionario
    
    if ($i % 500 -eq 0) {
        Write-Host "  Processados $i de $NUM_FUNCIONARIOS funcionários..." -ForegroundColor Gray
    }
}

Write-Host "Funcionários gerados: $($funcionarios.Count)" -ForegroundColor Green
Write-Host "  - Ativos: $(($funcionarios | Where-Object { $_.Status -eq 'Ativo' }).Count)" -ForegroundColor Green
Write-Host "  - Desligados: $(($funcionarios | Where-Object { $_.Status -eq 'Desligado' }).Count)" -ForegroundColor Green

# Gerar Turnover
Write-Host "`nGerando tabela de Turnover..." -ForegroundColor Yellow
$turnover = @()
$turnoverId = 1

$desligados = $funcionarios | Where-Object { $_.Status -eq 'Desligado' }
foreach ($func in $desligados) {
    $dataAdmissao = [DateTime]::Parse($func.Data_Admissao)
    $diasTotal = ($DATA_FIM - $dataAdmissao).Days
    $diasDesligamento = $random.Next(1, $diasTotal)
    $dataDesligamento = $dataAdmissao.AddDays($diasDesligamento)
    
    $tempoCasaDias = ($dataDesligamento - $dataAdmissao).Days
    $tipo = if ($random.NextDouble() -gt 0.4) { 'Voluntário' } else { 'Involuntário' }
    $salarioBase = $random.Next(3000, 25001)
    $custo = [Math]::Round($salarioBase * ($random.NextDouble() * 2 + 0.5), 2)
    $risco = [Math]::Round($random.NextDouble() * 100, 2)
    
    $turnover += [PSCustomObject]@{
        ID = $turnoverId++
        Funcionario_ID = $func.ID
        Data_Desligamento = $dataDesligamento.ToString('yyyy-MM-dd')
        Tipo_Turnover = $tipo
        Area = $func.Setor
        Tempo_Casa_Dias = $tempoCasaDias
        Custo_Desligamento = $custo
        Risco_Rotatividade = $risco
    }
}

# Adicionar registros de risco para ativos
$ativos = $funcionarios | Where-Object { $_.Status -eq 'Ativo' } | Get-Random -Count ([Math]::Min(200, ($funcionarios | Where-Object { $_.Status -eq 'Ativo' }).Count))
foreach ($func in $ativos) {
    if ($random.NextDouble() -gt 0.7) {
        $dataAdmissao = [DateTime]::Parse($func.Data_Admissao)
        $diasTotal = ($DATA_FIM - $dataAdmissao).Days
        $diasAvaliacao = $random.Next(1, $diasTotal)
        $dataAvaliacao = $dataAdmissao.AddDays($diasAvaliacao)
        $risco = [Math]::Round($random.NextDouble() * 65 + 20, 2)
        
        $turnover += [PSCustomObject]@{
            ID = $turnoverId++
            Funcionario_ID = $func.ID
            Data_Desligamento = $null
            Tipo_Turnover = $null
            Area = $func.Setor
            Tempo_Casa_Dias = ($dataAvaliacao - $dataAdmissao).Days
            Custo_Desligamento = 0
            Risco_Rotatividade = $risco
        }
    }
}

Write-Host "Turnover gerado: $($turnover.Count) registros" -ForegroundColor Green

# Gerar T&D
Write-Host "Gerando tabela de T&D..." -ForegroundColor Yellow
$td = @()
$tdId = 1

foreach ($func in $funcionarios) {
    $numTreinamentos = $random.Next(0, 9)
    $dataAdmissao = [DateTime]::Parse($func.Data_Admissao)
    
    for ($j = 0; $j -lt $numTreinamentos; $j++) {
        $diasTotal = ($DATA_FIM - $dataAdmissao).Days
        $diasInicio = $random.Next(0, $diasTotal)
        $dataInicio = $dataAdmissao.AddDays($diasInicio)
        
        $rand = $random.NextDouble()
        if ($rand -lt 0.80) {
            $status = 'Concluído'
            $horas = [Math]::Round($random.NextDouble() * 36 + 4, 2)
            $diasConclusao = $random.Next(1, ($DATA_FIM - $dataInicio).Days)
            $dataConclusao = $dataInicio.AddDays($diasConclusao)
            $avaliacao = [Math]::Round($random.NextDouble() * 4 + 6, 2)
            $aderencia = [Math]::Round($random.NextDouble() * 40 + 60, 2)
        } elseif ($rand -lt 0.95) {
            $status = 'Em Andamento'
            $horas = [Math]::Round($random.NextDouble() * 18 + 2, 2)
            $dataConclusao = $null
            $avaliacao = $null
            $aderencia = [Math]::Round($random.NextDouble() * 90, 2)
        } else {
            $status = 'Cancelado'
            $horas = [Math]::Round($random.NextDouble() * 9 + 1, 2)
            $dataConclusao = $null
            $avaliacao = $null
            $aderencia = [Math]::Round($random.NextDouble() * 40, 2)
        }
        
        $td += [PSCustomObject]@{
            ID = $tdId++
            Funcionario_ID = $func.ID
            Treinamento_ID = $random.Next(1, 101)
            Nome_Treinamento = $TREINAMENTOS[$random.Next($TREINAMENTOS.Length)]
            Data_Inicio = $dataInicio.ToString('yyyy-MM-dd')
            Data_Conclusao = if ($dataConclusao) { $dataConclusao.ToString('yyyy-MM-dd') } else { $null }
            Horas_Capacitacao = $horas
            Aderencia_Plano_Educacional = $aderencia
            Avaliacao_Eficacia = $avaliacao
            Status = $status
        }
    }
}

Write-Host "T&D gerado: $($td.Count) registros" -ForegroundColor Green

# Gerar PDI
Write-Host "Gerando tabela de PDI..." -ForegroundColor Yellow
$pdi = @()
$pdiId = 1

foreach ($func in $funcionarios) {
    $numPdis = $random.Next(0, 4)
    $dataAdmissao = [DateTime]::Parse($func.Data_Admissao)
    
    for ($j = 0; $j -lt $numPdis; $j++) {
        $diasTotal = ($DATA_FIM - $dataAdmissao).Days
        $diasInicio = $random.Next(0, $diasTotal)
        $dataInicio = $dataAdmissao.AddDays($diasInicio)
        
        $mesesDuracao = $random.Next(3, 13)
        $dataConclusaoPlanejada = $dataInicio.AddMonths($mesesDuracao)
        if ($dataConclusaoPlanejada -gt $DATA_FIM) {
            $dataConclusaoPlanejada = $DATA_FIM
        }
        
        $rand = $random.NextDouble()
        if ($rand -lt 0.70) {
            $status = 'Concluído'
            $diasConclusao = $random.Next(0, [Math]::Min(($dataConclusaoPlanejada.AddDays(60) - $dataInicio).Days, ($DATA_FIM - $dataInicio).Days))
            $dataConclusaoReal = $dataInicio.AddDays($diasConclusao)
            if ($dataConclusaoReal -gt $DATA_FIM) { $dataConclusaoReal = $DATA_FIM }
            $aderencia = [Math]::Round($random.NextDouble() * 30 + 70, 2)
            $evolucao = [Math]::Round($random.NextDouble() * 4 + 6, 2)
        } elseif ($rand -lt 0.90) {
            $status = 'Em Andamento'
            $dataConclusaoReal = $null
            $aderencia = [Math]::Round($random.NextDouble() * 60 + 20, 2)
            $evolucao = [Math]::Round($random.NextDouble() * 4 + 4, 2)
        } else {
            $status = 'Cancelado'
            $dataConclusaoReal = $null
            $aderencia = [Math]::Round($random.NextDouble() * 40, 2)
            $evolucao = [Math]::Round($random.NextDouble() * 4 + 2, 2)
        }
        
        $pdi += [PSCustomObject]@{
            ID = $pdiId++
            Funcionario_ID = $func.ID
            PDI_ID = $random.Next(1, 501)
            Area = $func.Setor
            Lideranca = Gerar-Nome
            Data_Inicio = $dataInicio.ToString('yyyy-MM-dd')
            Data_Conclusao_Planejada = $dataConclusaoPlanejada.ToString('yyyy-MM-dd')
            Data_Conclusao_Real = if ($dataConclusaoReal) { $dataConclusaoReal.ToString('yyyy-MM-dd') } else { $null }
            Status = $status
            Aderencia_Percentual = $aderencia
            Evolucao_Competencias = $evolucao
        }
    }
}

Write-Host "PDI gerado: $($pdi.Count) registros" -ForegroundColor Green

# Gerar Clima
Write-Host "Gerando tabela de Clima..." -ForegroundColor Yellow
$clima = @()
$climaId = 1

$datasPesquisa = @(
    [DateTime]::Parse("2022-06-01"), [DateTime]::Parse("2022-12-01"),
    [DateTime]::Parse("2023-06-01"), [DateTime]::Parse("2023-12-01"),
    [DateTime]::Parse("2024-06-01"), [DateTime]::Parse("2024-12-01")
)

foreach ($dataPesquisa in $datasPesquisa) {
    $funcionariosAtivos = $funcionarios | Where-Object { 
        [DateTime]::Parse($_.Data_Admissao) -le $dataPesquisa 
    }
    
    $participantes = $funcionariosAtivos | Get-Random -Count ([Math]::Floor($funcionariosAtivos.Count * 0.7))
    
    foreach ($func in $participantes) {
        $npsLideranca = $random.Next(0, 11)
        $resultadoClima = [Math]::Round($random.NextDouble() * 4.5 + 5, 2)
        
        $alertas = $null
        if ($random.NextDouble() -lt 0.10) {
            $alertasList = @('Baixa participação em reuniões', 'Isolamento da equipe', 'Falta de comunicação', 'Desmotivação observada', 'Conflitos interpessoais')
            $alertas = $alertasList[$random.Next($alertasList.Length)]
        }
        
        $clima += [PSCustomObject]@{
            ID = $climaId++
            Funcionario_ID = $func.ID
            Data_Pesquisa = $dataPesquisa.ToString('yyyy-MM-dd')
            NPS_Lideranca = $npsLideranca
            Resultado_Pesquisa_Clima = $resultadoClima
            Alertas_Comportamentais = $alertas
        }
    }
}

Write-Host "Clima gerado: $($clima.Count) registros" -ForegroundColor Green

# Gerar Inovação e Competências
Write-Host "Gerando tabela de Inovação e Competências..." -ForegroundColor Yellow
$inovacao = @()
$inovacaoId = 1

foreach ($func in $funcionarios) {
    $numSkills = $random.Next(3, 11)
    $skillsFunc = $SKILLS | Get-Random -Count $numSkills
    $dataAdmissao = [DateTime]::Parse($func.Data_Admissao)
    
    foreach ($skill in $skillsFunc) {
        $numAvaliacoes = $random.Next(1, 13)
        
        for ($k = 0; $k -lt $numAvaliacoes; $k++) {
            $diasTotal = ($DATA_FIM - $dataAdmissao).Days
            $diasAvaliacao = $random.Next(0, $diasTotal)
            $dataAvaliacao = $dataAdmissao.AddDays($diasAvaliacao)
            
            $nivelCompetencia = [Math]::Round($random.NextDouble() * 7 + 3, 2)
            $gapCritico = $random.NextDouble() -lt 0.20
            $performance = [Math]::Round($random.NextDouble() * 6 + 4, 2)
            
            $inovacao += [PSCustomObject]@{
                ID = $inovacaoId++
                Funcionario_ID = $func.ID
                Skill_ID = $random.Next(1, 1001)
                Nome_Skill = $skill
                Nivel_Competencia = $nivelCompetencia
                Gap_Critico = $gapCritico
                Performance_Trilha_Estrategica = $performance
                Data_Avaliacao = $dataAvaliacao.ToString('yyyy-MM-dd')
            }
        }
    }
}

Write-Host "Inovação e Competências gerado: $($inovacao.Count) registros" -ForegroundColor Green

# Salvar em CSV
Write-Host ""
Write-Host "Salvando arquivos CSV..." -ForegroundColor Yellow

$funcionarios | Export-Csv -Path "funcionarios.csv" -NoTypeInformation -Encoding UTF8
$turnover | Export-Csv -Path "turnover.csv" -NoTypeInformation -Encoding UTF8
$td | Export-Csv -Path "td.csv" -NoTypeInformation -Encoding UTF8
$pdi | Export-Csv -Path "pdi.csv" -NoTypeInformation -Encoding UTF8
$clima | Export-Csv -Path "clima.csv" -NoTypeInformation -Encoding UTF8
$inovacao | Export-Csv -Path "inovacao_competencias.csv" -NoTypeInformation -Encoding UTF8

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "ESTATÍSTICAS GERADAS:" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Funcionários: $($funcionarios.Count)"
Write-Host "  - Ativos: $(($funcionarios | Where-Object { $_.Status -eq 'Ativo' }).Count)"
Write-Host "  - Desligados: $(($funcionarios | Where-Object { $_.Status -eq 'Desligado' }).Count)"
Write-Host "Turnover: $($turnover.Count) registros"
Write-Host "T&D: $($td.Count) registros"
Write-Host "PDI: $($pdi.Count) registros"
Write-Host "Clima: $($clima.Count) registros"
Write-Host "Inovação e Competências: $($inovacao.Count) registros"
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Arquivos CSV gerados com sucesso!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan

