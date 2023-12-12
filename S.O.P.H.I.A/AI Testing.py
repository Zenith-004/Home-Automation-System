import openai
import pyttsx3
import pyaudio
import speech_recognition as sr 
import datetime
import time

from pyfirmata import Arduino,util
import serial
import time 

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
    
    else:
        # AI Code
        openai.api_key ="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"
        response= openai.Completion.create(engine="text-davinci-003",prompt=command,max_tokens=1000)
        final_response=response.choices[0]['text']
        print(final_response)

        # Final Reply
        talk(final_response)
        talk("is there any thing else i can help you with?")

        
