import cv2
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize the hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Allow camera to warm up
time.sleep(2.0)

# Start video capture
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Detect hands
    hands, img = detector.findHands(frame)

    # Draw a text box at the bottom
    cv2.rectangle(img, (400, 425), (640, 480), (50, 50, 255), -2)

    if hands:
        lmList = hands[0]["lmList"]  # Correct way to extract landmarks
        fingerUp = detector.fingersUp(hands[0])

        # Map finger positions to text
        messages = {
            (0, 0, 0, 0, 0): "LIGHT: OFF",
            (0, 1, 0, 0, 0): "WHAT",
            (0, 1, 1, 0, 0): "IS",
            (0, 1, 1, 1, 0): "PHOTOSYNTHESIS",
            (0, 1, 1, 1, 1): "LIGHT ON",
            (1, 1, 1, 1, 1): "LIGHT ON",
        }

        text = messages.get(tuple(fingerUp), "")
        cv2.putText(frame, text, (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Show the frame
    cv2.imshow("Frame", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
