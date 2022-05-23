import cv2
import HandTrackingModule as htm
import numpy as np
from pynput.mouse import Button, Controller
import wx
from time import sleep
cap = cv2.VideoCapture(0)
cap.set(3,1200)
cap.set(3,720)


#########################################
mouse=Controller()
app=wx.App(False)
(sx,sy)=wx.GetDisplaySize()
(camx,camy)=(320,240)
##########################################

detector = htm.handDetector(detectionCon=0.6)
pinchFlag=0
while True:
     success,img = cap.read()
     img = detector.findHands(img)
     lmList = detector.findPosition(img, draw=True)
     if lmList:

          x1, y1=lmList[8][1],lmList[8][2]
          x2, y2 = lmList[4][1], lmList[4][2]
          if (x1-x2)<=5 and (y1-y2)<=5:
               mouse.press(Button.left)
               sleep(0.6)
               mouseLoc = (sx - (x1 * sx / camx), y1 * sy / camy)
               mouse.position = mouseLoc

          else:
               mouse.release(Button.left)
               mouseLoc = (sx - (x1 * sx / camx), y1 * sy / camy)
               mouse.position = mouseLoc

          cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
     cv2.imshow("image",img)
     cv2.waitKey(1)