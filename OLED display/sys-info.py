from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time
import socket
import subprocess
#decodigo.com
serial = i2c(port=1, address=0x3C)
#device = ssd1306(serial, rotate=0)
device = sh1106(serial, width=128, height=64, rotate=0)
#device.capabilities(width=128, height=64, rotate=0)
print("size: " , device.bounding_box)
device.clear()


def stats(device):
    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memor>
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell = True )
    with canvas(device) as draw:        
        # Pi Stats Display
        draw.text((0, 0), "IP: " + str(IP,'utf-8'), fill="white")
        draw.text((0, 16), str(CPU,'utf-8') + "LA", fill="white")
        draw.text((80, 16), str(Temp,'utf-8') , fill="white")
        draw.text((0, 32), str(MemUsage,'utf-8'), fill="white")
        draw.text((0, 48), str(Disk,'utf-8'), fill="white")
while True:
    stats(device)
    time.sleep(1.0)