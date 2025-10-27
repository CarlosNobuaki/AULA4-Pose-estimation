# Pose Estimation - CIAg# Pose Estimation com MediaPipe Tasks - CIAg



Uma aplicação web em tempo real para detecção de poses humanas usando **MediaPipe Tasks** e **Flask**, desenvolvida para a aula de Computer Vision do Synapse e (CIAg).Uma aplicação web em tempo real para detecção de poses humanas.



![Pose Estimation Demo](https://img.shields.io/badge/Status-Funcionando-brightgreen)

![Python](https://img.shields.io/badge/Python-3.7+-blue)

![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange)

![Flask](https://img.shields.io/badge/Flask-3.0+-red)




## Funcionalidades

- **Detecção de múltiplas pessoas**: Até **15 pessoas simultaneamente**- **Controles por teclado** para melhor experiência

- **Pose estimation em tempo real**: Usando MediaPipe Tasks

- **FPS counter**: Monitoramento de performance em tempo real

- **Controles por teclado**: Atalhos para melhor experiência- Webcam funcionando


## Tecnologias Utilizadas## Instalação


- **Backend**: Python 3.7+, Flask, MediaPipe Tasks1. **Clone ou baixe os arquivos do projeto**

- **Frontend**: HTML5, CSS3, JavaScript ES6

- **Computer Vision**: MediaPipe Pose Landmarker (modelo completo)2. **Instale as dependências:**

- **Streaming**: MJPEG over HTTP```bash

pip install opencv-python mediapipe flask numpy

## Pré-requisitos```



- Python 3.7 ou superior3. **Verifique a estrutura do projeto:**

- Webcam funcionando```

- Navegador web moderno (Chrome, Firefox, Safari, Edge)pose_estimation/

- Sistema operacional: Linux, macOS, Windows├── pose_inference.py      # Aplicação principal

├── run_app.py            # Script de inicialização

## Instalação├── requirements.txt      # Dependências

├── templates/

### 1. Clone ou baixe o projeto│   └── index.html       # Interface web

```bash
git clone [URL_DO_PROJETO]
cd AULA4-Computer_Vision_pose_estimation
```

### 2. Execução automática (Recomendado)

```bash
./start_app.sh
```

### 3. Execução manual

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
./start_app.sh
# ou
python3 pose_inference.py
```

## Como Usar

### Método 1: Script de inicialização (Recomendado)

```bash
./start_app.sh
```

### Método 2: Diretamente

```bash
python pose_inference.py
```

### Método 3: Via terminal

```bash
cd /caminho/para/o/projeto
python -m flask --app pose_inference run --host=0.0.0.0 --port=5000
```

