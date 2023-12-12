import openai
import pyttsx3
import speech_recognition as sr 

# Speaker Code
speaker = pyttsx3.init()
speaker.setProperty('rate', 140)
speaker.setProperty('volume', 0.7)

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

speaker.setProperty('voice', voice_id)

speaker.say("Hello Sheldon")
speaker.say("I am Sofia")
speaker.say("What can I help you with")

speaker.runAndWait()

# Functions
def talk(text):
    speaker.say(text)
    speaker.runAndWait() 

# Listener Code
listener=sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice =listener.listen(source) 
        command=listener.recognize_google(voice)
        print(command)
except:
    pass

# AI Code
openai.api_key ="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"
response= openai.Completion.create(engine="text-davinci-003",prompt=command,max_tokens=1000)
final_response=response.choices[0]['text']
print(final_response)

# Final Reply
talk(final_response)
