# 2108_python_beaglebone

A BareBone Python example for 21xx/11xx/41xx/47xx on BeagleBone

**Prerequisites**:

Install Python 3.8 following the instruction on https://linuxize.com/post/how-to-install-python-3-8-on-debian-10/

Install Pyserial via **pip3 install pyserial**, more info about pyserial can be found in https://pypi.org/project/pyserial/. Please note that **pip3** instead of **pip** is used here due to Python 3.x installs PiP3.

Turn 21xx/11xx/41xx/47xx into CDC mode: plug the device to USB port, if the LED already blinks Yellow, stop, you are already in CDC mode. If not, once the LED turns blinking Green, push and hold the button immediately (within 5 second time frame), the LED should turn white, hold until LED turns Red, then release the button, now the LED will blink yellow to indicate CDC mode. If you need to exit CDC mode, repeate the same action and a green blinking LED will indicate LibUSB mode.

For communication protocol, please refer to https://www.dataq.com/resources/pdfs/misc/Dataq-Instruments-Protocol.pdf

**To try it out**:

Use WinSCP https://sourceforge.net/projects/winscp/ to send 2108_beaglebone.py to a folder on BeagleBone

To run it, use **python3 2108_beaglebone.py**

**Note**:

If you see error message complaining “failed "import serial module" or "seial doesn't have the attribue of serial", You may need to run "pip3 unstall serial" and "pip3 unstall serial" then reinstall pyserial to make sure pyserial is the ONLY to serial module installed on BeagleBone.

BeagleBone may have earlier version Python installed, so make sure you use **python3** instead of **python** to start the program

We need to force Python to construct 8-bit ASCII string by inserting b in front of the string, such as b"stop\r" instead of "stop/r"

Since we use readline, Python looks for CR/LF, so we need to use "eol 1" command 

"encode" determines the output format, where
0 outputs raw ADC reading in two-byte binary format
3 outputs raw ADC reading in ASCII format
1 & 2 outputs voltage instead of raw ADC reading shown in the protocol

0 results in highest performance, and 1 & 2 the lowest, with 3 in between

/dev/ttyACM0 or /dev/ttyACM1? read more in https://arstechnica.com/civis/viewtopic.php?f=16&t=1403645 and https://gist.github.com/edro15/1c6cd63894836ed982a7d88bef26e4af

