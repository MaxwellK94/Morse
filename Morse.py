
import RPi.GPIO as GPIO
import time

ledPin = 11  

def setup():
    GPIO.setmode(GPIO.BOARD)       
    GPIO.setup(ledPin, GPIO.OUT)   
    GPIO.output(ledPin, GPIO.LOW)  
    
def morse():
    while True:
        #Morse code consists of dashes and dots - a long and a short signal
        #The length of a dash is three times the length of a dot
        morseDict = {
        "a": (1,3),
        "b": (3,1,1,1),
        "c": (3,1,3,1),
        "d": (3,1,1),
        "e": (1,),
        "f": (1,1,3,1),
        "g": (3,3,1),
        "h": (1,1,1,1),
        "i": (1,1),
        "j": (1,3,3,3),
        "k": (3,1,3),
        "l": (1,3,3,3),
        "m": (3,3),
        "n": (3,1),
        "o": (3,3,3),
        "p": (1,3,3,1),
        "q": (3,3,1,3),
        "r": (1,3,1),
        "s": (1,1,1),
        "t": (3,),
        "u": (1,1,3),
        "v": (1,1,1,3),
        "w": (1,3,3),
        "x": (3,1,1,3),
        "y": (3,1,3,3),
        "z": (3,3,1,1),
        " ": (4,)
        }
        #high speed ==> more frequent flashing
        speed = 4
        message = input("input message \n").lower()
        for i in message:
            for j in morseDict[i.lower()]:
                GPIO.output(ledPin, GPIO.HIGH)  # led on
                print (i,"corresponds to ",morseDict[i],j)
                time.sleep(j/speed) 
                GPIO.output(ledPin, GPIO.LOW) # led off
                print ('led off...')
                time.sleep(1/speed)
            time.sleep(3/speed)


def destroy():
    GPIO.output(ledPin, GPIO.LOW)     
    GPIO.cleanup()                    

if __name__ == '__main__':   
    setup()
    try:
        morse()
    except KeyboardInterrupt: 
        destroy()
