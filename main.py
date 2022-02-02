import cv2
import dlib

cap = cv2.VideoCapture(0) #captura de tela pela webcam

detector = dlib.get_frontal_face_detector()

while True:
	_, frame = cap.read() #captura a foto

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grava os frames em escala de cinza
	faces = detector(gray)

	for face in faces:
		x, y = face.left(), face.top()
		x1, y1 = face.right(), face.bottom()
		cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

	cv2.imshow("Frame", frame) #mostra a foto na tela

	key = cv2.waitKey(1)
	if key==27: #cancela ao apertar esc
		break

cap.release()
cv2.destroyAllWindows()