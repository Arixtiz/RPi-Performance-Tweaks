# OLED Display and System Information for Raspberry Pi with Luma 🚀📊

Welcome to PiMastery, your guide to OLED displays and harnessing system information on Raspberry Pi. Explore overclocking, stats visualization, and powerful scripts. Join our community for Pi adventures!

## Installing Dependencies

If pip can't install dependencies automatically, manually add them:

```bash
$ sudo apt-get update
$ sudo apt-get full-upgrade
$ sudo apt-get install python3 python3-pip python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y
$ sudo pip3 install --upgrade setuptools
$ sudo pip3 install --upgrade adafruit-python-shell
```

For non-Raspberry Pi OS, consult your Linux distro's docs for the correct procedure.

Tip: If your distro has Pillow, use it instead of pip. Example:


```bash
$ sudo apt-get install python3-imaging
# or
$ sudo apt-get install python3-pil
```

## Permissions

luma.oled needs hardware access permission. After installation, add the user to required groups:

```bash
$ sudo usermod -a -G spi,gpio,i2c pi
```
Replace pi with your account name.

# Pin Connection for OLED Display on Raspberry Pi 📌

Ensure to connect the Raspberry Pi GPIO pins to the Display according to the following table:

| Pin | Name | Meaning   | Raspberry Pi Pin | Raspberry Pi Function |
| --- | ---- | --------- | ----------------- | ---------------------- |
| 1   | GND  | Ground    | P01-6             | GND                    |
| 2   | VCC  | +3.3V Power| P01-1             | 3V3                    |
| 3   | SCL  | Clock     | P01-5             | GPIO 3 (SCL)           |
| 4   | SDA  | Data      | P01-3             | GPIO 2 (SDA)           |

Ensure to follow these connections to ensure proper operation of the OLED display with your Raspberry Pi.

# Library Documentation for OLED Display on Raspberry Pi 📘

For additional documentation on the library, please visit: [Luma OLED Documentation](https://luma-oled.readthedocs.io/en/latest/)

Explore the comprehensive documentation to unlock the full potential of the Luma OLED library for your Raspberry Pi project. Learn about features, configuration options, and best practices to enhance your OLED display experience.

# Run on Init - Automatic Execution on Raspberry Pi Startup

## Overview

Automate the execution of a Python script on Raspberry Pi startup using cron. This simple guide will help you set up a cron job to run your script every time the Pi boots up.

## Steps

1. Open the crontab configuration:
```bash
$ crontab -e
```
Add the following line to the crontab file:
```bash
@reboot python3 /home/pi/sys_info.py &
```
This line ensures that the Python script (sys_info.py in this case) will be executed in the background every time the Raspberry Pi reboots.

Save the changes and exit the editor.

For Nano, press Ctrl + X, then Y, and finally Enter.

For Vim, type :wq and press Enter.

The script will now run automatically on Raspberry Pi startup.

Note
Ensure the script's path and name are correct, and the Python interpreter is installed. Adjust the path and script name in the cron command accordingly.

Feel free to adapt this guide to suit your specific requirements.

# Raspberry Pi I2C Configuration for Ubuntu or Non-Raspberry Pi OS 🚀

If your Raspberry Pi is running an operating system like Ubuntu or different from the Raspberry Pi OS and you need to enable I2C, follow these instructions:

1. Navigate to [raspi-config on archive.raspberrypi.org](https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/?C=M;O=D). Choose the latest version.

```bash
wget https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_*INSERT DATE*_all.deb -P /tmp
```

2. Attempt to install using dpkg, which may report missing dependencies. Read the output and install the dependencies:
```bash
sudo dpkg -i /tmp/raspi-config_*INSERT DATE*_all.deb
sudo apt-get install *INSERT DEPENDENCIES*
sudo apt-get -fy
sudo dpkg -i /tmp/raspi-config_*INSERT DATE*_all.deb
```
3. Run raspi-config:
```bash
sudo raspi-config
```
4. Navigate to 'Interfacing Options', enable I2C.
5. Install relevant packages. At a minimum, you'll want i2c-tools. Additionally, consider getting libi2c-dev and python3-smbus if Python is your language of choice.
```bash
sudo apt-get install i2c-tools libi2c-dev python3-smbus
```
6. Try probing the I2C bus as both a regular user and root:
```bash
sudo i2cdetect -y 1  # or 0, I2C bus number is hardware-dependent
```
If you encounter a permission error, proceed to the next step; otherwise, skip it.

7. Create an I2C usergroup, apply it to the bus, and add your user to this group:
```bash
sudo groupadd i2c  # group may exist already
sudo chown :i2c /dev/i2c-1  # or i2c-0
sudo chmod g+rw /dev/i2c-1
sudo usermod -aG i2c *INSERT YOUR USERNAME*
```
8. Log out and log in. If you were connected via VS Code's SSH extension, a reboot might be necessary. Then retry:
```bash
sudo i2cdetect -y 1  # or 0, I2C bus number is hardware-dependent
```