def lights():
    from pyfirmata import Arduino,util
    import serial
    import time 
    board= Arduino('COM3')
    print(board.get_firmata_version())
    board.digital[13].write(0)

"""
loopTimes=input("how many times do you want the led to blink: ")
print("Blinking "+loopTimes+" times ")

for x in range(int(loopTimes)):
    board.digital[13].write(1)
    time.sleep(0.2)
    board.digital[13].write(0)
    time.sleep(0.2)
"""
