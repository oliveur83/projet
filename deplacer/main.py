### ce fichier est le coeur du projet 
import cv2
import cvzone
import numpy as np
import HandTrackingModule as htm
import math


################################
#taille de la camera
wCam, hCam = 1200, 480
################################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(detectionCon=0.7)
colorR = (255, 0, 255)

################################################################################################
cx, cy, w, h = 100, 100, 200, 200


class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor


#test de boucle en permanence
while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList)!=0:
        #longerur
        x1, y1 = lmList[8][0], lmList[8][1]
        x2, y2 = lmList[4][0], lmList[4][1]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        length = math.hypot(x2 - x1, y2 - y1)
        print(length)
        cursor = lmList[8]
        if length <= 20:
            print("toto",cursor)
            if  cx - w//2 <cursor[1]< cx+w and cy - h <cursor[2]<cy+h//2:
                colorR = 0,255,0
                cx = cursor[1]
                cy= cursor [2]
            else:
                colorR = (255, 0, 255)

    cv2.rectangle(img, (cx - w // 2, cy - h // 2),(cx + w // 2, cy + h // 2), colorR, cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.waitKey(1)