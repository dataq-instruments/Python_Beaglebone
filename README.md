# 2108_python_beaglebone

A BareBone Python example for 21xx/11xx/41xx/47xx on BeagleBone

**Prerequisites**:

Install Python 3.8 following the instruction on https://linuxize.com/post/how-to-install-python-3-8-on-debian-10/

Install Pyserial via "pip3 install pyserial", more info about pyserial can be found in https://pypi.org/project/pyserial/. Please note that we use "pip3" instead of "pip" here due to Python 3.x installs PiP3.

Turn 21xx/11xx/41xx/47xx into CDC mode: plug the device to USB port, if the LED already blinks Yellow, stop, you are already in CDC mode. If not, once the LED turns blinking Green, push and hold the button immediately (within 5 second time frame), the LED should turn white, hold until LED turns Red, then release the button, now the LED will blink yellow to indicate CDC mode. If you need to exit CDC mode, repeate the same action and a green blinking LED will indicate LibUSB mode.

**To try it out**:

Use WinSCP to send 2108_beaglebone.py to a folder in BeagleBone

To run it, use **Python3 2108_beaglebone.py**

**Note**:

If you see error message complaining “failed "import serial module" or "seial doesn't have the attribue of serial", You may need to run "pip3 unstall serial" and "pip3 unstall serial" then reinstall pyserial to make sure pyserial is the ONLY to serial module installed on BeagleBone.

BeagleBone may have earlier version Python installed, so make sure you use Python3 instead of Python to start the program

