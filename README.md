TB_NFC_Cardreader
==============
NFC card reader for Tinkerboard. This script written with python language to build check in system for employees.

**Important notice:** This library is based on an existing library of ***Mario Gómez***
https://github.com/mxgxw/MFRC522-python

## Requirements
This library directed to Tinkerboard boards.

- Install python.
- Install GPIO of ASUS
- Change the RPi.GPIO to ASUS.GPIO
- Go to the file MFRC522.py, on line 130 change spidev from 1.0 to 2.0. This interface is enabled by default.

## Pins(GPIO.BOARD)
You can use [this](http://radioaficion.com/news/wp-content/uploads/2017/01/Asus_Tinker_Board_catalogue-3.jpg) image for reference.

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |


## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.
