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

```bash├── static/

git clone [URL_DO_PROJETO]│   └── logo_ciag_branco.svg  # Logo CIAg

cd AULA4-Computer_Vision_pose_estimation└── README.md            # Este arquivo

``````



### 2. Execução automática (Recomendado)## Como usar

```bash

./start_app.sh### Método 1: Script de inicialização (Recomendado)

``````bash

python run_app.py

### 3. Execução manual```

```bash

# Criar ambiente virtual### Método 2: Diretamente

python3 -m venv venv```bash

source venv/bin/activate  # Linux/Macpython pose_inference.py

# ou```

venv\\Scripts\\activate   # Windows

### Método 3: Via terminal

# Instalar dependências```bash

pip install -r requirements.txtcd /caminho/para/o/projeto

python -m flask --app pose_inference run --host=0.0.0.0 --port=5000

# Executar aplicação```

python3 pose_inference.py

```## Acesso



## Como UsarApós iniciar a aplicação, acesse:

- **Local:** http://localhost:5000

1. **Inicie a aplicação**: Execute `./start_app.sh`- **Rede local:** http://SEU_IP:5000

2. **Acesse no navegador**: http://localhost:5000

3. **Posicione-se**: Fique em frente à câmera## Controles

4. **Veja a detecção**: Os landmarks da pose aparecerão em tempo real

| Tecla | Função |

### Controles de Teclado|-------|--------|

| `F` | Alternar tela cheia |

| Tecla | Função || `R` | Resetar visualização |

|-------|--------|| `ESC` | Sair da tela cheia |

| `F` | Alternar tela cheia |

| `R` | Recarregar página |## Interface

| `ESC` | Sair da tela cheia |

- **Tela principal:** Visualização da câmera com detecções

### Tela Principal- **Indicadores:** FPS, número de poses detectadas

- **Vídeo em tela cheia**: Ocupa toda a área disponível- **Ângulos:** Exibidos próximos às articulações

- **Landmarks coloridos**: Pontos e conexões da pose em tempo real

- **Contador de pessoas**: "Pessoas detectadas: X/15" no vídeo## Configuração Avançada



### MediaPipe Tasks### Ajustar sensibilidade da detecção

```pythonPara MediaPipe Tasks (linha ~30):

base_options = python.BaseOptions(model_asset_path="pose_landmarker_full.task")

options = vision.PoseLandmarkerOptions(

    base_options=base_options,
    num_poses=15,  # Até 15 pessoas, 
    output_segmentation_masks=False,
    min_pose_detection_confidence=0.5,
    min_pose_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

```### Personalizar cores dos landmarks

No método `_draw_angles` (linha ~80):

### Câmera```python

- **Resolução**: 1280x720 (padrão)mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2)

- **FPS**: 20-30 FPS (dependendo do hardware)```

- **Formato**: MJPEG streaming

``````bash

pose_estimation/# Testar câmera manualmente

├── pose_inference.py           # Aplicação principal Flaskpython -c "import cv2; cap=cv2.VideoCapture(0); print('Câmera OK' if cap.isOpened() else 'Câmera ERRO')"

├── start_app.sh               # Script de inicialização```

├── requirements.txt           # Dependências Python

├── README.md                  # Este arquivo### MediaPipe Tasks não disponível

├── venv/                      # Ambiente virtualO código faz fallback automático para MediaPipe clássico se Tasks não estiver disponível.

├── templates/

│   └── index.html            # Interface web### Erro de permissão da câmera

├── static/- Linux: Adicionar usuário ao grupo `video`

│   └── logo_ciag_branco.svg  # Logo CIAg- Windows: Verificar configurações de privacidade

└── pose_landmarker_full.task # Modelo MediaPipe (baixado automaticamente)- Mac: Permitir acesso à câmera nas configurações

```bash

