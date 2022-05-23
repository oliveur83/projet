import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import math

wCam, hCam = 1200, 480
################################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
#################################
detector = FaceMeshDetector(maxFaces=1)
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
color = (255, 0, 255)

ratioList = []
blinkCounter =0
while True:
    success, img = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    img, faces = detector.findFaceMesh(img,draw=False)
    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 5, color, cv2.FILLED)

        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]
        lengtver = math.hypot(leftDown[0] - leftUp[0],leftDown[1]- leftUp[1])
        lenghtHor =math.hypot(leftRight[0] - leftLeft[0],leftRight[1]- leftLeft[1])

        ratio = int((lengtver / lenghtHor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)
        if ratioAvg < 35 :
            blinkCounter += 1
        print(blinkCounter)
    img = cv2.flip(img, 1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)