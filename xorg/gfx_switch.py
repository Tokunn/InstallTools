#!/usr/bin/env ipython3
# -*- coding: utf-8 -*-

### New Python Template File
### H27 Mar 16

import os, sys

status = ['stamina', 'speed']

def main():
    switch = get_ipython().getoutput('cat /sys/devices/platform/sony-laptop/gfx_switch_status')
    if (switch[0] == status[0]):
        print("Stamina")
        get_ipython().system(' cp /etc/X11/xorg.conf.stamina /etc/X11/xorg.conf')
    else:
        print("Speed")
        get_ipython().system(' cp /etc/X11/xorg.conf.speed /etc/X11/xorg.conf')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl+C -> END")

