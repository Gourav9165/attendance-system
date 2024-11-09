from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Student, Attendance
from .forms import StudentRegistrationForm
from .utils import detect_faces, train_model, mark_attendance
import cv2
import numpy as np
import os
from django.conf import settings

def home(request):
    return render(request, 'face_recognition/home.html')

@require_http_methods(["GET", "POST"])
def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            
            # Initialize camera
            cap = cv2.VideoCapture(0)
            count = 0
            
            while count < 30:  # Take 30 sample images
                ret, frame = cap.read()
                faces, gray = detect_faces(frame)
                
                for (x, y, w, h) in faces:
                    count += 1
                    cv2.imwrite(
                        os.path.join(settings.MEDIA_ROOT, f'training_images/{student.id}.{count}.jpg'),
                        gray[y:y+h, x:x+w]
                    )
            
            cap.release()
            train_model()
            messages.success(request, 'Student registered successfully!')
            return redirect('home')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'face_recognition/register.html', {'form': form})

def take_attendance(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(os.path.join(settings.MEDIA_ROOT, 'trainer/trainer.yml'))
    
    cap = cv2.VideoCapture(0)
    attendance_taken = False
    
    while True:
        ret, frame = cap.read()
        faces, gray = detect_faces(frame)
        
        for (x, y, w, h) in faces:
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            
            if confidence < 50:
                mark_attendance(id)
                attendance_taken = True
            
        if attendance_taken or (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    messages.success(request, 'Attendance taken successfully!')
    return redirect('home')

def view_attendance(request):
    attendance = Attendance.objects.all().order_by('-date', '-time')
    return render(request, 'face_recognition/attendance.html', {'attendance': attendance})