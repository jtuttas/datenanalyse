import cv2
import easyocr
import matplotlib.pyplot as plt

#read image
imagelocation = 'car2.jpg'
img = cv2.imread(imagelocation)

#instance text detector
reader = easyocr.Reader(['en'], gpu=False)

#detect text on image
text = reader.readtext(img)

print(text)