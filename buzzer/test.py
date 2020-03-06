import RPi.GPIO as GPIO
import time

buzzer_pin = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

frequency = 440
period = 1.0 / frequency
delayValue = period / 2

print("sleep", delayValue)

try:
    while True:
        GPIO.output(buzzer_pin, True)
        time.sleep(delayValue)
        GPIO.output(buzzer_pin, False)
        time.sleep(delayValue)
except KeyboardInterrupt:
    print(" bye")
finally:
    GPIO.cleanup()
