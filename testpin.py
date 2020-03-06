import RPi.GPIO as GPIO
import time
import sys

test_pin = int(sys.argv[1])
print(f'testing pin {test_pin}')

GPIO.setmode(GPIO.BCM)
GPIO.setup(test_pin, GPIO.IN)
GPIO.setup(test_pin, GPIO.OUT)


try:
  while True:
    GPIO.output(test_pin, True)
    time.sleep(0.2)
    GPIO.output(test_pin, False)
    time.sleep(0.2)
except KeyboardInterrupt:
  print("bye")
finally:
  GPIO.output(test_pin, False)
  GPIO.cleanup()
