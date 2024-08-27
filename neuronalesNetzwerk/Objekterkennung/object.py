import requests
import cv2
import numpy as np

# IP-Adresse und Port der Android IP Webcam
ip = "192.168.178.80"  # Ersetze dies durch die IP-Adresse deiner Webcam
port = "8080"

# URL zum Abrufen des Bildes
url = f"http://{ip}:{port}/shot.jpg"

# Lade den vortrainierten Gesichtserkennungs-Klassifikator
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Funktion zum Abrufen des Bildes und Durchführung der Gesichtserkennung


def fetch_and_detect_faces():
    response = requests.get(url)
    img_array = np.array(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        num_faces = len(faces)
        cv2.putText(img, f'Faces: {num_faces}', (10, 160),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('IP Webcam - Face Detection', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        return False
    return True


if __name__ == "__main__":
    while True:
        if not fetch_and_detect_faces():
            break

    cv2.destroyAllWindows()
