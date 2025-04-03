from pyfirmata import Arduino,util
import serial
import time 
board= Arduino('COM3')
board.digital[9].write(1)

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

# Test for input string 'hello'
input_string = 'hello'

for char in input_string:
    char_lower = char.lower()
    if char_lower in letters_leds:
        turn_off_leds()
        turn_on_leds(letters_leds[char_lower])
        time.sleep(1)  # Adjust delay time as needed
    else:
        turn_off_leds()
        time.sleep(1)  # Adjust delay time as needed
