import os
import cv2

# Сначала получаем путь до картинки, и лучше перевести его в абсолютный
# переменная __file__ возвращает путь к нашему скрипту
# os.path.normpath - корректирует наш относительный путь до картинки
# os.path.join создаёт абсолютный путь до картинки
#
n = os.path.join(os.path.dirname(__file__), os.path.normpath('./Pics/CrazyCats.jpg'))
img = cv2.imread(n)
print('Open image: ', img.shape)

#img = cv2.resize(img, (200,300)) # изменяем её размер
#print(img.shape)

# показываем картинку
cv2.imshow('Crazy cat!', img)

# ждём (мсек), 0 - до нажатия любой клавиши
cv2.waitKey(0)
