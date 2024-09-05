# 🌟 Sofia - Your Personal Home Assistant! 🌟

Welcome to **Sofia** — a friendly home assistant designed to make life easier, especially for disabled individuals. Whether you need to turn on the lights, translate text into Braille, or control your computer with just hand gestures, Sofia’s got your back! Built with accessibility in mind, Sofia brings AI magic into your life and helps you navigate the world with ease. ✨

## 🎉 What Can Sofia Do?
Sofia comes packed with superpowers designed for **effortless use**, making her perfect for disabled individuals or anyone who loves convenience!

### 🗣️ Chat Like a Pro!
Talk to Sofia and she talks back! From light control to casual conversations, she listens to you like the best buddy ever. No complicated commands or typing needed — just your voice.

### 💡 Light Control via Voice
With just a few simple words, Sofia can turn on or off your Arduino-powered lights. Whether you have mobility challenges or just want to stay comfy, Sofia handles the lights for you!  
Say it loud:  
*“Hey Sofia, turn on the light!”*  
*“Sofia, turn off the light!”*

### 🔤 Braille Translator Mode (Mode 4)
Got a word? Sofia’s got the translation! Designed for individuals with visual impairments, Sofia can translate spoken words into Braille using LEDs. Inclusivity at its finest! 💡🔡

### 🖱️ Jedi-Level Mouse Control (Mode 3)
Wave your hand and control your mouse like a Jedi! No need for touchpads or mice — use hand gestures to move your mouse and click. Perfect for anyone with limited dexterity. The Force is strong with this one!

### 🖐️ Gesture-Powered Light Control (Mode 2)
Hand gestures aren’t just for talking — they can now control your lights too! Put up a few fingers, and Sofia gets the message. This feature is especially useful for individuals with limited mobility. ✋💡

### 🤖 Ask Sofia Anything!
Not sure what to do? Need some life advice? Sofia taps into OpenAI's powers to generate smart, friendly, and sometimes funny responses to your questions. She’s like your personal AI assistant with a bit more flair! ✨

---

## 🛠️ What You’ll Need
Before you and Sofia can start transforming your life, here’s what you need:

### Hardware:
- **Arduino board** (We used an Arduino UNO, but feel free to use your fave!).
- LEDs for Braille display (perfect for visually impaired users).
- A **Microphone** for voice commands.
- A **Webcam** for Jedi-level hand gestures.

### Software:
- **Python Libraries** to install:
   ```bash
   pip install pyttsx3 pyaudio SpeechRecognition pyfirmata openai cv2 numpy cvzone mouse
   ```
- Upload the **Standard Firmata** firmware to your Arduino using the Arduino IDE.

- Don’t forget your **OpenAI API Key!** 🔑  
   Add it to the script like so:
   ```python
   openai.api_key = "your-api-key-here"
   ```

---

## 🚀 Let’s Get This Party Started!
1. Clone this repository and hop into the code.
2. Connect your Arduino, LEDs, microphone, and webcam.
3. Run Sofia:
   ```bash
   python sofia_assistant.py
   ```
4. Say “Hi Sofia” and let the magic begin! 🎇

---

## 🗣️ Here’s What You Can Say to Sofia
- **Meet Sofia**: "Sofia please introduce yourself!"
- **Voice to Text Magic**: "convert voice to text"
- **Light Control**: "turn on/off the light"
- **Braille Mode (Mode 4)**: "execute mode 4" (Sofia will light up the LEDs for you!)
- **Mouse Control Mode (Mode 3)**: "execute mode 3" (Start moving the mouse with your hands like a boss!)
- **Light Control with Gestures (Mode 2)**: "execute mode 2" (Wave your hands to turn the lights on/off)
- **Say Goodbye**: "bye," "no thank you," "goodbye!"

---

## ✨ Fun Features:
- **AI Conversations**: Sofia can have fun chats with you! If she doesn't know the answer to your command, she’ll come up with a creative response using OpenAI's GPT-3!
- **Hand Gestures**: Control things around you like a real-life wizard! 🧙‍♂️ No touch required.
- **Braille Translation**: Sofia takes inclusivity seriously. She translates spoken words into Braille, lighting up your world in more ways than one.

---

## 🖥️ How It Works
- Sofia listens for your voice, understands what you're saying, and responds with a smile (figuratively speaking).
- She talks to an **Arduino** to control connected devices (like lights).
- Hand gestures are tracked using **OpenCV** to let you control your computer like you’re in a sci-fi movie.

---

## 📋 License
Feel free to make Sofia your own. This project is licensed under the MIT License, so go ahead and build cool things with her!

---

**Sofia** is your personal home assistant, but she’s especially tailored for those who need a little extra help — making life easier, brighter, and more accessible. 😄 Let’s bring Sofia to life and start making everyday tasks a lot more fun and effortless!

---