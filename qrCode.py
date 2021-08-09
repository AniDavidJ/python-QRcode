#open CV       pip install opencv-python
#numpy         pip install numpy
#pyzbar        pip install pyzbar

import cv2
import numpy as np
from pyzbar.pyzbar import decode

#read image from file
#img = cv2.imread(r'C:\Users\TOSHIBA\Desktop\PythonProject\QRCode\download.png')

# caputre video
cap = cv2.VideoCapture(0)
cap.set(3,640)  # 3 - Width
cap.set(4,480)  # 4 - Height


while True:
    sucess,img = cap.read()
    
    #print(codeinform)
    codeinform = decode(img)
    for singleData in codeinform:
        pts = np.array([singleData.polygon],np.int32)
        cv2.polylines(img,[pts],True,(0,255,0),3)
        
        myText = singleData.data.decode('utf-8')
        rect = singleData.rect
        cv2.putText(img,myText,(rect[0],rect[1]),cv2.FONT_HERSHEY_DUPLEX,0.9,(0,255,0),3,)
        print(myText)
      
    cv2.imshow('Result image',img)
    cv2.waitKey(2)

