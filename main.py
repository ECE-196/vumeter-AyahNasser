import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,

    # do the rest...
]




leds = [DigitalInOut(pin) for pin in led_pins]
for led in leds:
    led.direction = Direction.OUTPUT


while True:
    volume = microphone.value
    for i, led in enumerate(leds):
        print(volume)

        j = volume*len(leds)//49574

        print(j)
        if i < j:
            led.value = True
        else:
            led.value = False
    sleep(0.2) 

    #leds[3].value = not leds[0].value


#main loop
#while True:
    #volume = microphone.value

    #print(volume)

    #leds[0].value = not leds[0].value
    #leds[1].value = not leds[0].value


    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
