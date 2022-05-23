import cv2
import cvzone
import HandTrackingModule as htm
from time import sleep
import numpy as np
from pynput.keyboard import Controller
################################
wCam, hCam = 1200, 720
################################
finalText = ""
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


keyboard = Controller()
detector = htm.handDetector(detectionCon=0.4)
keys = [["a","z","e","r","t","y","u","i","o","p","<"],
        ["q","s","d","f","g","h","j","k","l","m"],
        ["w","x","c","v","b","n",",",";",":","!","enter"]]

#def drawAll(img, buttonList):
 #   for button in buttonList:
   #     x, y = button.pos
    #    w, h = button.size
#
  #      cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
 #       cv2.putText(img, button.text, (x + 20, y + 65),
 #                   cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
 #   return img


def drawAll(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos
        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                           20, rt=0)
        cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
                       (255, 0, 255), cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 40, y + 60),
                     cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    out = img.copy()
    alpha = 0.1
    mask = imgNew.astype(bool)
    print(mask.shape)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return out

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text



buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=True)
    img = drawAll(img, buttonList)

    if lmList:
        for button in buttonList:
            x,y=button.pos
            w,h= button.size

            if x < lmList[4][1] < x + w and y < lmList[4][2] < y + h:
                if x < lmList[8][1] < x + w and y < lmList[8][2] < y + h:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    l, _, _ = detector.findDistance(8, 12, img)
                    if l < 32:
                        keyboard.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65),
                                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        if button.text=="<":
                            finalText=finalText[:len(finalText)-1]
                            
                        else:
                            finalText += button.text
                        sleep(0.6)

    cv2.rectangle(img, (50,350), (700,450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

    cv2.imshow("Img", img)
    cv2.waitKey(1)