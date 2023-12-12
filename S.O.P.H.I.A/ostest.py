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
talk("How can i help you?")

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
    

    if "Sophia please introduce yourself" in command:
        talk("Hello, I am Sofia")
        talk("system organised functional and informative assistant")
        talk("I was created by Mister Sheldon Ashish Stephen on twenty first april two thousand and twenty three")
        talk("it is a pleasure to meet you all")
        talk("please let me know if you need anything")
    
    elif command in["voice text converter","convert voice to text"]:
        try:
            with sr.Microphone() as source:
                talk("listening")
                print("Listening...")
                voice =listener.listen(source) 
                command =listener.recognize_google(voice)
                print(command)
        except:
            pass
        talk("any thing else sir?")
        event = input("Press enter to talk:")
        if event == "":
            continue
        else:
            pass

    elif command in ["no thank you Sophia","no Sophia","no thank you","no","bye","no thanks Sophia"]:
        talk("ok please let me now if you need anything else")
        talk("bye")
        break
    
    elif command in ["hello Sophia","Hi Sophia"]:
        talk("hello what can I help you with?")
        event = input("Press enter to talk:")
        if event == "":
            continue
        else:
            pass

    
    elif command in ["what is your name"]:
        talk("my name is Sophia")
        talk("system organised functional and informative assistant")
        talk("is there something i can help you with?")
        event = input("Press enter to talk:")
        if event == "":
            continue
        else:
            pass

    elif command in ["Sophia"]:
        talk("yes it is me Sofia what can i help you with?")
        event = input("Press enter to talk:")
        if event == "":
            continue
        else:
            pass
    
    else:
        # AI Code
        openai.api_key ="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"
        response= openai.Completion.create(engine="text-davinci-003",prompt=command,max_tokens=1000)
        final_response=response.choices[0]['text']
        print(final_response)

        # Final Reply
        talk(final_response)
        talk("is there any thing else i can help you with?")

        
