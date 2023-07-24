import cv2
from win10toast import ToastNotifier

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
toaster = ToastNotifier()

known_faces = {
    "1": "Qua",
    "2": "Salam",
}

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_id = "1"
        if face_id in known_faces:
            name = known_faces[face_id]
            toaster.show_toast("Qua Face Scanner", f"Merhaba {name}!", duration=5, threaded=True)
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            
    cv2.imshow('Qua Face Scanner', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Program Çıkışı (q)
        break

cap.release()
cv2.destroyAllWindows()
