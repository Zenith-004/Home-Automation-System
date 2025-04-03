# Sofia AI - Your Personal Assistant 🤖

Welcome to Sofia, your very own **System Organized Assistant**! 🚀
Sofia is a voice-activated AI designed to assist you with a variety of tasks, from controlling lights to translating text into Braille. With an intuitive speech recognition system and a smart interaction model, Sofia is here to make your life easier! 

---

## 🎙️ Features

### 1. **Voice Commands** 🗣️
Sofia listens to your commands and responds accordingly. Just say *"Hello Sofia"* and start interacting!

### 2. **Arduino Integration** ⚡
Control your Arduino-connected devices effortlessly. Turn lights on/off with a simple voice command or even with hand gestures!

### 3. **Hand Gesture Recognition** ✋
Sofia can interpret hand gestures using a camera and turn lights on/off based on your finger movements.

### 4. **Virtual Mouse Control** 🖱️
Move your cursor and click using just hand movements. No mouse? No problem!

### 5. **Braille Mode** 🔠
Convert spoken words into Braille patterns using LEDs, making it a great learning tool for the visually impaired.

### 6. **AI Chat Integration** 🧠
Need information, conversation, or just a bit of AI-generated wisdom? Sofia is powered by the Ollama AI model to provide smart responses!

---

## 🎛️ How to Use

### **1. Run the Script**
- Ensure you have all dependencies installed (see Installation section below).
- Open a terminal or command prompt.
- Run Sofia using:
  ```bash
  python main.py
  ```
  (The main code is located in `main.py`. Other execution files include `braille.py` for Braille mode and `ollama_test.py` for AI chat testing.)

### **2. Interact with Sofia**
- **Start the Conversation:** Say *"Hello Sofia"* to wake her up.
- **Give Commands:** Sofia responds to various commands like:
  - "Turn on the light"
  - "Execute mode 2"
  - "Translate to Braille"
  - "What is your name?"
- **Voice Confirmation:** Sofia will acknowledge and execute commands while responding verbally.

### **3. Use Different Modes**
#### 🔆 **Mode 1 - Light Control (Voice & Gesture)**
- Use voice commands like *"Sofia, turn on the light"* to control an Arduino-connected LED.
- Hand gestures (open/closed palm) can also toggle the light.

#### 🖐️ **Mode 2 - Hand Gesture Recognition**
- Enables webcam-based hand detection.
- Controls lights and displays messages based on finger gestures.
- Open palm = Light ON, Closed fist = Light OFF.

#### 🖱️ **Mode 3 - Virtual Mouse Control**
- Uses webcam to track hand movement for controlling the cursor.
- Bringing fingers together simulates a mouse click.
- Exit by pressing `Q` on the keyboard.

#### 🔠 **Mode 4 - Braille Translator**
- Sofia listens to your voice and translates words into Braille using LEDs.
- Each letter is represented by a specific LED pattern.
- Speak clearly to get accurate results.

### **4. Exit Sofia**
- Say *"Goodbye Sofia"*, *"No, thank you Sofia"*, or *"Bye"* to stop Sofia and close the program.

---

## 🔌 Arduino Connections
Sofia integrates with an Arduino board to control LEDs and other hardware components. To set it up:

### **Required Components:**
- **Arduino Board** (Uno, Mega, or similar)
- **LEDs** (for light control & Braille mode)
- **Jumper Wires**
- **Breadboard**

### **Wiring Setup:**
- **LED for Light Control:**
  - Connect the **positive (long leg)** of an LED to **digital pin 9**.
  - Connect the **negative (short leg)** to **GND**.
- **Braille Mode LEDs:**
  - Connect LEDs to **pins 2, 3, 4, 5, 6, and 7** (one for each Braille dot).
  - Ensure each LED is connected properly to GND.
- **Powering the Arduino:**
  - Connect the LEDs to **3.3V** using a breadboard.
  - Use a **USB cable** to connect to your computer.
  - Ensure the correct **COM port** is used in the script (`COM3` for Windows, `/dev/ttyUSB0` for Linux/Mac).

### **Uploading Standard Firmata Before Use**
Before running Sofia, you need to upload the **Standard Firmata** firmware to your Arduino:
1. Open **Arduino IDE**.
2. Go to **File > Examples > Firmata > StandardFirmata**.
3. Select the correct **board** and **port** from the **Tools** menu.
4. Click **Upload** and wait for the process to complete.

---

## 🛠️ Installation
To run Sofia, ensure you have the following installed:
- Python 3.x
- `pyttsx3` (Text-to-Speech)
- `pyaudio` (Audio Input)
- `speech_recognition` (Voice Commands)
- `pyfirmata` (Arduino Integration)
- `cv2` & `cvzone` (Hand Tracking)
- `ollama` (AI Chat)
- `mouse` (Virtual Mouse Control)

Install dependencies with:
```bash
pip install pyttsx3 pyaudio speech_recognition pyfirmata opencv-python cvzone ollama mouse
```

---

## 💡 Fun Easter Eggs!
Try saying:
- *"Sofia, introduce yourself"* for a special intro!
- *"Sofia, what is photosynthesis?"* for a cool light trick! 🌱

Enjoy using Sofia! 😃✨

