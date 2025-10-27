#!/bin/bash

echo "Iniciando Pose Estimation - CIAg"
echo "=================================="

# Ativar ambiente virtual
if [ -d "venv" ]; then
    echo "🔧 Ativando ambiente virtual..."
    source venv/bin/activate
fi

# Verificar dependências
python3 -c "import cv2, mediapipe, flask, numpy; print('✅ Dependências OK!')" 2>/dev/null || {
    echo "Instalando dependências..."
    pip install opencv-python mediapipe flask numpy
}

# Executar aplicação
echo "Iniciando servidor..."
echo "Acesse: http://localhost:5000"
echo "Pressione Ctrl+C para parar"
echo "=================================="

python3 pose_inference.py