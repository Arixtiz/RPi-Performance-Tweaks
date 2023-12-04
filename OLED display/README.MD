# OLED Display and System Information for Raspberry Pi 🚀📊

Welcome to PiMastery, your guide to OLED displays and harnessing system information on Raspberry Pi. Explore overclocking, stats visualization, and powerful scripts. Join our community for Pi adventures!

## Installing Dependencies

If pip can't install dependencies automatically, manually add them:

```bash
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y

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