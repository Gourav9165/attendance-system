import cv2
import numpy as np
import os
from django.conf import settings
from .models import Student, Attendance
from datetime import datetime

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def detect_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces, gray

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = os.path.join(settings.MEDIA_ROOT, 'training_images')

    assure_path_exists(path)
    
    face_samples = []
    ids = []
    
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            img_path = os.path.join(path, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            student_id = int(filename.split('.')[0])
            face_samples.append(img)
            ids.append(student_id)
            
    recognizer.train(face_samples, np.array(ids))
    recognizer.save(os.path.join(settings.MEDIA_ROOT, 'trainer/trainer.yml'))

def mark_attendance(student_id):
    try:
        student = Student.objects.get(id=student_id)
        now = datetime.now()
        attendance = Attendance.objects.create(
            student=student,
            date=now.date(),
            time=now.time()
        )
        return True
    except:
        return False