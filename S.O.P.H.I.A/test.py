import cv2
import numpy as np
import mouse
from cvzone.HandTrackingModule import HandDetector

def mouse_movement(image, x, y, w, h, sensitivity):
    cx, cy = int(x + w / 2), int(y + h / 2)
    x_move, y_move = cx - image.shape[1] / 2, cy - image.shape[0] / 2
    x_move *= sensitivity # Reverse left and right movements
    y_move *= sensitivity
    mouse.move(x_move, y_move, absolute=False, duration=0)

def mouse_click(image, lmList):
    x1, y1 = lmList[8][0], lmList[8][1]
    x2, y2 = lmList[17][0], lmList[17][1]
    distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < 50: # Adjust this value to change the threshold for the click
        mouse.click('left')

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

sensitivity = 0.04 # Adjust this value to decrease sensitivity

while True:
    ret, image = cap.read()
    if ret:
        hands, _ = detector.findHands(image)
        if hands:
            hand = hands[0]
            lmList = hand["lmList"]
            x, y = lmList[8][0], lmList[8][1]
            w, h = lmList[12][0] - lmList[8][0], lmList[12][1] - lmList[8][1]
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            mouse_movement(image, x, y, w, h, sensitivity)
            mouse_click(image, lmList)

        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()