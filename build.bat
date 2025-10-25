@echo off
REM
REM Script para compilar la aplicación Advanced Video Downloader en Windows.
REM
REM Uso:
REM 1. Simplemente haz doble clic en este archivo `build.bat` desde el explorador.
REM

echo =================================================
echo INICIANDO COMPILACION DE ADVANCED VIDEO DOWNLOADER
echo =================================================

REM Paso 1: Crear un entorno virtual si no existe
IF NOT EXIST "venv" (
    echo --> Creando entorno virtual...
    py -3 -m venv venv
) ELSE (
    echo --> Entorno virtual 'venv' ya existe.
)

REM Paso 2: Activar el entorno virtual
echo --> Activando entorno virtual...
call "venv\Scripts\activate.bat"

REM Paso 3: Instalar/actualizar dependencias
echo --> Instalando dependencias desde requirements.txt...
pip install --upgrade pip
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Fallo en la instalacion de dependencias.
    goto :error
)

REM Paso 4: Ejecutar PyInstaller
echo --> Compilando la aplicacion con PyInstaller...
pyinstaller video_downloader.spec --noconfirm
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: PyInstaller fallo durante la compilacion.
    goto :error
)

REM Paso 5: Desactivar el entorno virtual
call "venv\Scripts\deactivate.bat"

echo.
echo =================================================
echo ¡COMPILACION FINALIZADA CON EXITO!
echo =================================================
echo El ejecutable se encuentra en la carpeta: dist\
echo.
goto :end

:error
echo Compilacion fallida.
echo.

:end
pause
