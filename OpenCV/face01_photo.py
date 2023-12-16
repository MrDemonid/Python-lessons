import os
import cv2

# классификатор - это уже обученная на распознавание чего-то нейросеть

# подгружаем классификатор (определяющий что мы будем искать в изображении)
# в данном случае классификатор для распознавания лиц
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

n = os.path.join(os.path.dirname(__file__), os.path.normpath('./Pics/family.jpg'))
img = cv2.imread(n)

# переводим в градации серого, для облегчения поиска лиц
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# выполняем поиск в картинке
# координаты найденных объектов записываются в массив структур:
# (left, top, width, height)
faces = face_cascades.detectMultiScale(img_gray)
#print(faces)

# выводим рамки вокруг найденных объектов
for (left, top, width, height) in faces:
    cv2.rectangle(img, (left, top), (left+width, top+height), (0,250,255), 2)


cv2.imshow('Family photo', img)

cv2.waitKey(0)
