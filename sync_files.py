#!/usr/bin/env ipython3
# -*- coding: utf-8 -*-

import os, sys
import subprocess


def main():
    #print("\n###rc.lua")
    #get_ipython().system('mkdir -p /home/tokunn/.config/awesome')
    #get_ipython().system('cp /home/tokunn/Program/InstallTools/awesome/rc.lua /home/tokunn/.config/awesome/rc.lua')

    print("\n###vimperatorrc")
    get_ipython().system('cp /home/tokunn/Program/InstallTools/vimperator/.vimperatorrc /home/tokunn/.vimperatorrc')

    print("\n###conkyrc")
    get_ipython().system('cp /home/tokunn/Program/InstallTools/conky/.conkyrc /home/tokunn/.conkyrc')

    print("\n###vimrc")
    get_ipython().system('cp /home/tokunn/Program/InstallTools/vim/.vimrc /home/tokunn/.vimrc')

    #print("\n###vim/template")
    #get_ipython().system('mkdir -p /home/tokunn/.vim')
    #get_ipython().system('cp -r /home/tokunn/Program/InstallTools/vim/.vim/template /home/tokunn/.vim/template')

    print("\n###xinitrc")
    get_ipython().system('cp /home/tokunn/Program/InstallTools/xorg/.xinitrc /home/tokunn/.xinitrc')

    print("\n###zshrc")
    get_ipython().system('cp /home/tokunn/Program/InstallTools/zsh/.zshrc /home/tokunn/.zshrc')

    print("\n###qtile")
    get_ipython().system('mkdir -p /home/tokunn/.config/qtile')
    get_ipython().system('cp /home/tokunn/Program/InstallTools/qtile/config.py /home/tokunn/.config/qtile/')

if __name__ == '__main__':
    main()
