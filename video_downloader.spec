Aquí están los archivos finales para la compilación y distribución del proyecto.

---

### 1. `video_downloader.spec` (Archivo de Especificaciones para PyInstaller)

Este archivo, escrito en Python, le indica a PyInstaller cómo empaquetar la aplicación. Debe estar en la raíz del proyecto.

```python
# -*- mode: python ; coding: utf-8 -*-

# Este es el archivo de especificaciones para PyInstaller.
# Define cómo encontrar el código fuente, las dependencias y los recursos,
# y cómo construir el ejecutable final.

block_cipher = None


a = Analysis(['src/main.py'],
             pathex=['.'],  # Añade la raíz del proyecto al PYTHONPATH
             binaries=[],
             datas=[('resources', 'resources')], # Empaqueta la carpeta de recursos
             hiddenimports=[
                # Las importaciones ocultas son módulos que PyInstaller no detecta
                # automáticamente porque son importados de forma dinámica.
                'yt_dlp.extractor',
                'sqlalchemy.dialects.sqlite',
                'pkg_resources.py2_warn' # Necesario a veces para ciertas librerías
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# PYZ es un archivo comprimido que contiene todos los módulos de Python.
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# EXE define cómo se construye el archivo ejecutable.
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='AdvancedVideoDownloader', # Nombre del archivo ejecutable
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,  # Comprime el ejecutable (requiere UPX instalado)
          console=False, # False para una aplicación GUI (sin terminal)
          windowed=True,
          icon='resources/app_icon.ico') # Icono de la aplicación

# COLL es para agrupar todos los archivos en una sola carpeta (modo --onedir).
# No lo usamos aquí porque estamos generando un solo archivo (--onefile).
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='AdvancedVideoDownloader')

```

---

### 2. `build.sh` (Script de Compilación para Linux y macOS)

Este script automatiza todo el proceso de compilación en sistemas basados en UNIX.

```bash
#!/bin/bash
#
# Script para compilar la aplicación Advanced Video Downloader en Linux y macOS.
#
# Uso:
# 1. Asegúrate de que este script tenga permisos de ejecución: chmod +x build.sh
# 2. Ejecútalo desde la raíz del proyecto: ./build.sh
#

# Salir inmediatamente si un comando falla
set -e

echo "================================================="
echo "INICIANDO COMPILACIÓN DE ADVANCED VIDEO DOWNLOADER"
echo "================================================="

# Paso 1: Crear un entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "--> Creando entorno virtual..."
    python3 -m venv venv
else
    echo "--> Entorno virtual 'venv' ya existe."
fi

# Paso 2: Activar el entorno virtual
echo "--> Activando entorno virtual..."
source venv/bin/activate

# Paso 3: Instalar/actualizar dependencias
echo "--> Instalando dependencias desde requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# Paso 4: Ejecutar PyInstaller
echo "--> Compilando la aplicación con PyInstaller..."
pyinstaller video_downloader.spec --noconfirm

# Paso 5: Desactivar el entorno virtual
deactivate

echo ""
echo "================================================="
echo "¡COMPILACIÓN FINALIZADA CON ÉXITO!"
echo "================================================="
echo "El ejecutable se encuentra en la carpeta: dist/"
echo ""

```

---

### 3. `build.bat` (Script de Compilación para Windows)

Este script automatiza el proceso de compilación en sistemas Windows.

```batch
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
```
