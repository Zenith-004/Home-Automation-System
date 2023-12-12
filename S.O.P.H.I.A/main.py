import openai
import pyttsx3
import pyaudio
import speech_recognition as sr 
import datetime
import time

from pyfirmata import Arduino,util
import serial
import time 
#...................................................................................................................................

# Core Functions
# Speaker Code
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
speaker.setProperty('volume', 3)

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

speaker.setProperty('voice', voice_id)

# Talk Function 
def talk(text):
    speaker.say(text)
    speaker.runAndWait() 

# Wishing Function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speaker.say("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speaker.say("Good Afternoon Sir !")  
  
    else:
        speaker.say("Good Evening Sir !") 

talk("Hello Sheldon")
wishMe()
speaker.runAndWait()

#..........................................................................................................................
#Arduio Board Access
try:
    talk("trying to access Arduino board")
    board= Arduino('COM3')
    board.digital[9].write(1)
    talk("Access granted")
    talk("The Arduino board is now online sir")
except serial.serialutil.SerialException:
    talk("The Arduino Board seems to be offline sir")

talk("How can i help you?")


# Aurdino lights code
def lights(command):
    print(board.get_firmata_version())
    if command in ["Sofia turn on the light","turn on the light"]:
        talk("Turning on the lights sir")
        board.digital[9].write(0)
        talk("anything else sir?")
    elif command in ["Sofia turn off the light","turn off the light"]:
        talk("turning off the lights sir")
        board.digital[9].write(1)
        talk("anthing else sir?")

#.......................................................................................................

while True:
    # Listener Code
    global command 
    listener=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice =listener.listen(source) 
            command =listener.recognize_google(voice)
            print(command)
    except:
        pass
    

    if "Sofia please introduce yourself" in command:
        talk("Hello, I am Sofia")
        talk("system organised functional and informative assistant")
        talk("I was created by Mister Sheldon Ashish Stephen on twenty first april two thousand and twenty three")
        talk("it is a pleasure to meet you all")
        talk("please let me know if you need anything")
    
    elif command in["voice text converter","convert voice to text"]:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice =listener.listen(source) 
                command =listener.recognize_google(voice)
                print(command)
        except:
            pass
        talk("any thing else sir?")
    
    elif command in ["no thank you Sofia","no Sofia","no thank you","no","bye"]:
        talk("ok please let me now if you need anything else")
        talk("bye")
        break
    
    elif command in ["hello Sofia","Hi Sofia"]:
        talk("hello what can I help you with?")
    
    elif command in ["what is your name"]:
        talk("my name is Sofia")
        talk("system organised functional and informative assistant")
        talk("is there something i can help you with?")
    
    elif command in ["Sofia"]:
        talk("yes it is me Sofia what can i help you with?")
    
    elif command in ["Sofia turn on the light","Sofia turn off the light","turn on the light","turn off the light"]:
        lights(command)
    
    elif command in ["execute mode 4","execute mode four","execute mode for","braille mode","Braille mode"]:
        
        # Assuming the LED pins are connected to pins 2 to 7
        led_pins = [2, 3, 4, 5, 6, 7]

        def turn_on_leds(leds):
            for pin in leds:
                board.digital[pin].write(0)

        def turn_off_leds():
            for pin in led_pins:
                board.digital[pin].write(1)

        # LED configurations for each letter
        letters_leds = {
            'a': [2],
            'b': [2, 4],
            'c': [2, 3],
            'd': [1, 3, 5],
            'e': [2, 5],
            'f': [2, 4, 3],
            'g': [2, 4, 5, 3],
            'h': [2, 4, 5],
            'i': [4, 3],
            'j': [4, 3, 5],
            'k': [2, 6],
            'l': [2, 4, 6],
            'm': [2, 3, 6],
            'n': [2, 3, 5, 6],
            'o': [2, 5, 6],
            'p': [2, 3, 4, 6],
            'q': [2, 3, 4, 6, 5],
            'r': [2, 4, 6, 5],
            's': [3, 4, 6],
            't': [3, 4, 5, 6],
            'u': [2, 6,7],
            'v': [2, 4, 6, 7],
            'w': [3, 4, 5, 7],
            'x': [2, 3, 6, 7],
            'y': [2, 3, 5, 6, 7],
            'z': [2, 5, 6, 7]
        }
        
        talk("What do you want me to translate to braille")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice =listener.listen(source) 
                command1 =listener.recognize_google(voice)
                print(command1)
        except:
            pass
        

        for char in command1:
            char_lower = char.lower()
            if char_lower in letters_leds:
                turn_off_leds()
                turn_on_leds(letters_leds[char_lower])
                time.sleep(1)  # Adjust delay time as needed
            else:
                turn_off_leds()
                time.sleep(1)  # Adjust delay time as needed        
                        

    
    elif command in ["execute mode 3","execute mode three"]:
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
    

    elif command in ["execute mode 2","execute mode two","execute mode to"]:

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
                    board.digital[9].write(1)
                if fingerUp==[1,1,1,1,1]:
                    cv2.putText(frame, 'LIGHT ON', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                    board.digital[9].write(0)
                if fingerUp==[0,1,0,0,0]:
                    cv2.putText(frame, 'IS', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                if fingerUp==[0,1,1,1,0]:
                    cv2.putText(frame, 'PHOTOSYNTHESIS', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                if fingerUp==[0,1,1,1,1]:
                    cv2.putText(frame, 'LIGHT ON', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                if fingerUp==[1,1,1,1,1]:
                    cv2.putText(frame, 'LIGHT ON', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                if fingerUp==[1,0,0,0,1]:
                    cv2.putText(frame, 'QUIT', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                    video.release()
                    cv2.destroyAllWindows()
                    time.sleep(2.0)
                    talk("anthing else sir?")
                    break
                    

            cv2.imshow("Frame",frame)
            k=cv2.waitKey(1)
            if k==ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()


    else:
        # AI Code
        openai.api_key ="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"
        response= openai.Completion.create(engine="text-davinci-003",prompt=command,max_tokens=1000)
        final_response=response.choices[0]['text']
        print(final_response)

        # Final Reply
        talk(final_response)
        talk("is there any thing else i can help you with?")
