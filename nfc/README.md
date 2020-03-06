hardware: RFID-RC522

install these:
```
pip3 install mfrc522
pip3 install spidev
```

### pinout
| Name | Pin # | Pin name   |  GPIO
|:------:|:-------:|:------------:|
| SDA  | 24    | SPICEO     |   8
| SCK  | 23    | SPISCLK    |   11
| MOSI | 19    | SPIMOSI    |   10
| MISO | 21    | SPIMISO    |   9
| IRQ  | None  | None       |
| GND  |       | gnd        |
| RST  | 22    | GPIO25     |   25
| 3.3V |       | 3V3        |

datasheet: https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf

rpi pinouts: https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
