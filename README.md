TB_NFC_Cardreader
==============
NFC card reader for Tinkerboard. This script written with python language to build check in system for employees.

**Important notice:** This library is based on an existing library of [***Mario Gómez***](https://github.com/mxgxw/MFRC522-python)

## Requirements
This library directed to Tinkerboard boards.

- Install python.
    ```bash
        $ sudo apt-get update
        $ sudo apt-get install python-dev python3-dev
    ```
- Install Git app
    ```bash
        $ sudo apt-get git
    ```
- Download GPIO library for python from [ASUS website](https://www.asus.com/Single-Board-Computer/Tinker-Board/)
    ```bash
        $ git clone http://github.com/TinkerBoard/gpio_lib_python.git
    ```
- Navigate to folder
    ```bash
        $ cd gpio_lib_python/
    ```
- Install Python GPIO library for Tinker Board S
    ```bash
        $ sudo python setup.py install
        $ sudo python3 setup.py install 
    ```
- Install SPI from requirements folder taken from this [SPI Repo.](https://github.com/lthiery/SPI-Py) repo.
    ```bash
        $ cd requirements/SPI-Py/
        $ sudo python setup.py install
        $ sudo python3 setup.py install
    ```
- Finally (Optional) install requests library to make simple http request as i needed it in my application. Taken from this [Requests repo](https://github.com/requests/requests)
    ```bash
        $ cd requirements/requests/
        $ sudo python setup.py install
        $ sudo python3 setup.py install
    ```
- Enjoy by running this app using
    ```
        $ python Read.py
    ```

## Important to know!
when i was trying to run this application MFRC522 was designed for respberry Pi specifically so i did some changes which are:

- Inside MFRC522.py, change the RPi.GPIO to ASUS.GPIO.
- Go to the line 130 change spidev from 1.0 to 2.0. This interface is enabled by default.
- Dont forget to change you end-back end-point *-^.
- Now every thing setup.

## Pins(GPIO.BOARD)
You can use image as reference.
<h1 align="center">
    <br>
    <br>
    <img src="http://radioaficion.com/news/wp-content/uploads/2017/01/Asus_Tinker_Board_catalogue-3.jpg" alt="ASUS GPIO layout">
    <br>
    <br>
</h1>

And follow the map here to do the interface pins.

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | CE0        |
| SCK  | 23    | SCLK1      |
| MOSI | 19    | MOSI1      |
| MISO | 21    | MOSO1      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO5C3    |
| 3.3V | 1     | 3V3        |
| Buz  | 18    | GPIO5B3


## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.
