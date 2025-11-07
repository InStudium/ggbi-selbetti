@echo off
echo ========================================
echo Gerando Bases de Dados - People Analytics
echo ========================================
echo.

REM Verificar se Python esta instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado!
    echo.
    echo Por favor, instale Python 3.7 ou superior de:
    echo https://www.python.org/downloads/
    echo.
    echo Depois instale as dependencias:
    echo   pip install pandas numpy
    echo.
    pause
    exit /b 1
)

echo Python encontrado!
echo.

REM Verificar se pandas esta instalado
python -c "import pandas" >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando dependencias (pandas, numpy)...
    pip install pandas numpy
    if %errorlevel% neq 0 (
        echo ERRO ao instalar dependencias!
        pause
        exit /b 1
    )
)

echo Executando script de geracao...
echo.
python gerar_dados.py

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Arquivos CSV gerados com sucesso!
    echo ========================================
) else (
    echo.
    echo ERRO ao gerar os dados!
)

pause

