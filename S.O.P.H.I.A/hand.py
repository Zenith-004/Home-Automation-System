import cv2
from cvzone.HandTrackingModule import HandDetector
import time

detector=HandDetector(detectionCon=0.8, maxHands=1)


time.sleep(2.0)

current_key_pressed = set()

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    keyPressed = False
    spacePressed=False
    key_count=0
    key_pressed=0   
    hands,img=detector.findHands(frame)
    cv2.rectangle(img, (640, 480), (400, 425),(50, 50, 255), -2)
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame, 'LIGHT: OFF', (440,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[0,1,0,0,0]:
            cv2.putText(frame, 'WHAT', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[0,1,1,0,0]:
            cv2.putText(frame, 'IS', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[0,1,1,1,0]:
            cv2.putText(frame, 'PHOTOSYNTHESIS', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[0,1,1,1,1]:
            cv2.putText(frame, 'LIGHT ON', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[1,1,1,1,1]:
            cv2.putText(frame, 'LIGHT ON', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
