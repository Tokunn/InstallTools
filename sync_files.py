#!/usr/bin/env ipython3
# -*- coding: utf-8 -*-

### Sync Install Scripts
### H27 Mar 16

import os, sys
import subprocess


def main():
    print("\n###rc.lua")
    get_ipython().system('ls -l /home/tokunn/.config/awesome/rc.lua')
    get_ipython().system('cp /home/tokunn/.config/awesome/rc.lua /home/tokunn/Program/InstallTools/awesome/rc.lua')
    get_ipython().system('ls -l /home/tokunn/Program/InstallTools/awesome/rc.lua')

    print("\n###vimperatorrc")
    get_ipython().system('ls -l /home/tokunn/.vimperatorrc')
    get_ipython().system('cp /home/tokunn/.vimperatorrc /home/tokunn/Program/InstallTools/vimperator/.vimperatorrc')
    get_ipython().system('ls -l /home/tokunn/Program/InstallTools/vimperator/.vimperatorrc')

    print("\n###conkyrc")
    get_ipython().system('ls -l /home/tokunn/.conkyrc')
    get_ipython().system('cp /home/tokunn/.conkyrc /home/tokunn/Program/InstallTools/conky/.conkyrc')
    get_ipython().system('ls -l /home/tokunn/Program/InstallTools/conky/.conkyrc')

    print("\n###vimrc")
    get_ipython().system('ls -l /home/tokunn/.vimrc')
    get_ipython().system('cp /home/tokunn/.vimrc /home/tokunn/Program/InstallTools/vim/.vimrc')
    get_ipython().system('ls -l /home/tokunn/Program/InstallTools/vim/.vimrc')

    print("\n###vim/template")
    get_ipython().system('ls -l /home/tokunn/.vim/template')
    get_ipython().system('cp -r /home/tokunn/.vim/template/ /home/tokunn/Program/InstallTools/vim/.vim/')
    get_ipython().system('ls -l /home/tokunn/Program/InstallTools/vim/.vim/template')

    print("\n###xinitrc")
    get_ipython().system('ls -l /home/tokunn/.xinitrc')
    get_ipython().system('cp /home/tokunn/.xinitrc /home/tokunn/Program/InstallTools/xorg/.xinitrc')
    get_ipython().system('ls -l /home/tokunn/Program/InstallTools/xorg/.xinitrc')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl+C -> END")

