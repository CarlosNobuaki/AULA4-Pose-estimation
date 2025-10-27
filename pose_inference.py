import cv2
import mediapipe as mp
from mediapipe import solutions
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
import numpy as np
from flask import Flask, render_template, Response
import os
import urllib.request

app = Flask(__name__)

# Inicializar MediaPipe
mp_drawing = solutions.drawing_utils
mp_pose = solutions.pose

class PoseDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        # Download do modelo se não existir
        self._download_model_if_needed()
        
        # Usar MediaPipe Tasks com suporte para 15 pessoas
        base_options = python.BaseOptions(model_asset_path="pose_landmarker_full.task")
        options = vision.PoseLandmarkerOptions(
            base_options=base_options, 
            num_poses=15,  # Detectar até 15 pessoas
            min_pose_detection_confidence=0.5,
            min_pose_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.detector = vision.PoseLandmarker.create_from_options(options)
        print("✅ MediaPipe Tasks inicializado para 15 pessoas!")
    
    def _download_model_if_needed(self):
        """Download do modelo pose_landmarker_full.task se não existir"""
        model_path = 'pose_landmarker_full.task'
        if not os.path.exists(model_path):
            print("📥 Baixando modelo pose_landmarker_full.task...")
            url = 'https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task'
            try:
                urllib.request.urlretrieve(url, model_path)
                print("✅ Modelo baixado com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao baixar modelo: {e}")
                raise Exception("Não foi possível baixar o modelo")
    
    def detect_pose(self, frame):
        """Detecta pose na imagem e desenha os landmarks"""
        # Converter frame para RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        # Detectar poses
        detection_result = self.detector.detect(mp_image)
        
        pose_count = 0
        if detection_result.pose_landmarks:
            pose_count = len(detection_result.pose_landmarks)
            
            # Desenhar landmarks para cada pessoa detectada
            for pose_landmarks in detection_result.pose_landmarks:
                # Converter landmarks para formato compatível
                landmark_list = landmark_pb2.NormalizedLandmarkList()
                for landmark in pose_landmarks:
                    landmark_proto = landmark_pb2.NormalizedLandmark()
                    landmark_proto.x = landmark.x
                    landmark_proto.y = landmark.y
                    landmark_proto.z = landmark.z
                    landmark_list.landmark.append(landmark_proto)
                
                # Desenhar landmarks
                mp_drawing.draw_landmarks(
                    frame,
                    landmark_list,
                    mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=1)
                )
        
        # Adicionar contador de poses detectadas
        cv2.putText(frame, f'Pessoas detectadas: {pose_count}/15', 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        return frame
    
    def generate_frames(self):
        """Gera frames para streaming"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            # Flip horizontal para efeito espelho
            frame = cv2.flip(frame, 1)
            
            # Detectar pose
            frame = self.detect_pose(frame)
            
            # Codificar frame para JPEG
            ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    def __del__(self):
        if hasattr(self, 'cap'):
            self.cap.release()

# Instância global do detector
detector = None

def get_detector():
    """Inicializa o detector de pose sob demanda"""
    global detector
    if detector is None:
        detector = PoseDetector()
    return detector

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Feed de vídeo"""
    return Response(get_detector().generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("🚀 Iniciando Pose Estimation - CIAg")
    print("📱 Detecção para até 15 pessoas simultâneas")
    print("📱 Acesse: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
