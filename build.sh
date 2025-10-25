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
