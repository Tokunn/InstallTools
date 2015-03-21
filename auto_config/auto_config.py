#!/usr/bin/env ipython3
# -*- coding: utf-8 -*-

### Auto config
### H27 Mar 16

import os, sys

def main():
    get_ipython().system(' echo 25 > /sys/class/backlight/intel_backlight/brightness')
    get_ipython().system(' echo  0 > /sys/devices/platform/sony-laptop/kbd_backlight')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl+C -> END")

