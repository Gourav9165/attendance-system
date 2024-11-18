
---

# 📸 **Real-Time Face Recognition-Based Attendance System**  
### An automated solution for student attendance using face recognition.  

---

## 🌟 **Overview**  
The **Real-Time Face Recognition-Based Attendance System** leverages computer vision to capture and recognize student faces, ensuring seamless attendance tracking with minimal manual intervention. Built using **Django** and **OpenCV**, this project allows administrators to:  
- 🎓 Register students with face data.  
- ✅ Mark attendance automatically using real-time face recognition.  
- 📊 View and export attendance records.  

---

## 🚀 **Features**  
1. **Student Registration** 🎓  
   - Capture 30 face images per student for training.  
   - Store face data securely for recognition.  

2. **Real-Time Attendance** ✅  
   - Detect and recognize students using their face.  
   - Automatically mark attendance in the database.  

3. **Attendance Management** 📋  
   - View attendance records by date.  
   - Filter and search records.  
   - Export records as CSV files.  

---

## 🛠️ **Technologies Used**  
- **Backend:** Django, Python  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Database:** SQLite (can be replaced with other RDBMS)  
- **Libraries:** OpenCV, NumPy  

---

## 🗂️ **Project Structure**  
```plaintext
📁 project/
├── 📁 face_recognition/
│   ├── views.py         # Core logic for registration, attendance, and views
│   ├── utils.py         # Utility functions for face detection and training
│   ├── models.py        # Database models for Students and Attendance
│   ├── templates/       # HTML templates for UI
|   |   └── face_recognition/ 
│   │       ├── register.html
│   │       ├── home.html
│   │       └── attendance.html
├── 📁 media/            # Storage for training images and trained model
│   ├── training_images/ 
│   └── trainer.yml      # Trained face recognizer data
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

---

## 🎯 **Core Functionality**  

### 🖼️ **Student Registration**  
1. Navigate to **Register Student** in the app.  
2. Enter the student details and capture face data using the webcam.  
3. Train the face recognition model automatically.  

### 📷 **Take Attendance**  
1. Use the webcam to detect and recognize student faces.  
2. Attendance is marked automatically if the face is recognized.  

### 📑 **View Attendance**  
1. Check detailed attendance records with filters for date and name.  
2. Export attendance data as a CSV file for offline use.  

---

## 📦 **Setup Instructions**  

### Prerequisites  
- Python 3.8+  
- OpenCV  
- Django  

### Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/Gourav9165/attendance-system.git
   cd attendance-system
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the server:  
   ```bash
   python manage.py runserver
   ```

5. Access the app at:  
   `http://127.0.0.1:8000/`  

---

## 🎥 **How It Works**  

1. **Register a Student**  
   ![Registration GIF](media/Output/Registration.mp4)

2. **Take Attendance**  
   ![Attendance GIF](URL to GIF or Image)

3. **View Attendance Records**  
   ![Attendance Records GIF](URL to GIF or Image)

---

## 🛡️ **Security and Privacy**  
- Training images are stored locally in the `/media/training_images/` directory.  
- Face recognition data is saved in `trainer.yml` for quick processing.  

---

## 📝 **Future Enhancements**  
- Integrate with cloud storage for scalability.  
- Add notifications for attendance updates.  
- Support for multiple camera inputs.   

---

## 📜 **License**  
This project is licensed under the MIT License. See the `LICENSE` file for more details.  

---

## 🙌 **Acknowledgements**  
- **Django** for web framework.  
- **OpenCV** for face recognition.  
- **Bootstrap** for responsive design.   

--- 
