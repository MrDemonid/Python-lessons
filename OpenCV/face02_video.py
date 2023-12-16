import cv2

# классификатор - это уже обученная на распознавание чего-то нейросеть

# подгружаем классификатор (определяющий что мы будем искать в изображении)
# в данном случае классификатор для распознавания лиц
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

cam = cv2.VideoCapture(0)

while True:
    successed, frame = cam.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)
    for (left, top, width, height) in faces:
        cv2.rectangle(frame, (left, top), (left+width, top+height), (0,250,255), 2)
    cv2.imshow('Web-camera', frame)

    if ((cv2.waitKey(1) & 0xFF) == ord('q')):
        break
