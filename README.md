# 🌟 Sofia - Your Personal Home Assistant! 🌟

Welcome to **Sofia** — a friendly home assistant built to help you do awesome things! Whether you need to turn on the lights, translate text into Braille, or control your computer with just hand gestures, Sofia’s got your back! Designed for disabled individuals but loved by everyone, Sofia is here to bring a little AI magic into your life. ✨

## 🎉 What Can Sofia Do?
Sofia comes packed with superpowers:

1. **🗣️ Chat Like a Pro!**  
   Talk to Sofia and she talks back! From light control to casual conversations, she listens to you like the best buddy ever.
   
2. **💡 Light Control via Voice**  
   With just a few words, Sofia can turn on or off your Arduino-powered lights. No more getting up from your comfy couch!  
   Say it loud:  
   *“Hey Sofia, turn on the light!”*  
   *“Sofia, turn off the light!”*

3. **🔤 Braille Translator Mode (Mode 4)**  
   Got a word? Sofia’s got the translation! Tell her a word and watch (literally, on LEDs!) as she translates it into Braille. 💡🔡
   
4. **🖱️ Jedi-Level Mouse Control (Mode 3)**  
   Wave your hand and control your mouse like a Jedi! Use hand gestures to move your mouse around and even click — no touchpads or mice needed. **The Force is strong with this one!**

5. **🖐️ Gesture-Powered Light Control (Mode 2)**  
   Hand gestures aren’t just for talking — they can now control your lights too! Put up a few fingers, and Sofia gets the message. ✋💡

6. **🤖 Ask Sofia Anything!**  
   Not sure what to do? Need some life advice? Sofia taps into OpenAI's powers to generate some smart and maybe even funny responses to your questions. She's like your personal AI assistant but with more flair! ✨

## 🛠️ What You’ll Need
Before you and Sofia can rule the world together, here’s what you need:

### Hardware:
- **Arduino board** (We used an Arduino UNO, but feel free to use your fave!).
- LEDs for Braille display (get ready for some light shows!).
- A **Microphone** for voice commands.
- A **Webcam** for those Jedi-level hand gestures.

### Software:
- **Python Libraries** to install:
   ```bash
   pip install pyttsx3 pyaudio SpeechRecognition pyfirmata openai cv2 numpy cvzone mouse
   ```
- Upload the **Standard Firmata** firmware to your Arduino using the Arduino IDE.

- Don’t forget your **OpenAI API Key**! 🔑  
   Add it to the script like so:
   ```python
   openai.api_key = "your-api-key-here"
   ```

## 🚀 Let’s Get This Party Started!
1. Clone this repository and hop into the code.
2. Connect your Arduino, LEDs, microphone, and webcam.
3. Run Sofia:
   ```bash
   python sofia_assistant.py
   ```
4. Say “Hi Sofia” and let the magic begin! 🎇

## 🗣️ Here’s What You Can Say to Sofia
- **Meet Sofia**: "Sofia please introduce yourself!"
- **Voice to Text Magic**: "convert voice to text"
- **Light Control**: "turn on/off the light"
- **Braille Mode (Mode 4)**: "execute mode 4" (Sofia will light up the LEDs for you!)
- **Mouse Control Mode (Mode 3)**: "execute mode 3" (Start moving the mouse with your hands like a boss!)
- **Light Control with Gestures (Mode 2)**: "execute mode 2" (Wave your hands to turn the lights on/off)
- **Say Goodbye**: "bye," "no thank you," "goodbye!"

## ✨ Fun Features:
- **AI Conversations**: Sofia can have fun chats with you! If she doesn't know the answer to your command, she will come up with a creative response using OpenAI's GPT-3!
- **Hand Gestures**: Control things around you like a real-life wizard! 🧙‍♂️
- **Braille Translation**: Sofia takes inclusivity seriously. She translates spoken words into Braille, lighting up your world in more ways than one.

## 🖥️ How It Works
- Sofia listens for your voice, understands what you're saying, and responds with a smile (figuratively speaking).
- She talks to an **Arduino** to control connected devices (like lights).
- Hand gestures are tracked using **OpenCV** to let you control your computer like you’re in a sci-fi movie.

## 📋 License
Feel free to make Sofia your own. This project is licensed under the MIT License, so go ahead and build cool things with her!

---

Now, let’s bring Sofia to life and start making things a little easier and a lot more fun! 😄
