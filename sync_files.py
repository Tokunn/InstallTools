#!/usr/bin/env ipython3
# -*- coding: utf-8 -*-

import os, sys
import subprocess


def main():
    #print("\n###rc.lua")
    #get_ipython().system('mkdir -p ~/.config/awesome')
    #get_ipython().system('cp ~/Program/InstallTools/awesome/rc.lua ~/.config/awesome/rc.lua')

    print("\n###vimperatorrc")
    get_ipython().system('cp ~/Program/InstallTools/vimperator/.vimperatorrc ~/.vimperatorrc')

    print("\n###conkyrc")
    get_ipython().system('cp ~/Program/InstallTools/conky/.conkyrc ~/.conkyrc')

    print("\n###vimrc")
    get_ipython().system('cp ~/Program/InstallTools/vim/.vimrc ~/.vimrc')

    #print("\n###vim/template")
    #get_ipython().system('mkdir -p ~/.vim')
    #get_ipython().system('cp -r ~/Program/InstallTools/vim/.vim/template ~/.vim/template')

    print("\n###xinitrc")
    get_ipython().system('cp ~/Program/InstallTools/xorg/.xinitrc ~/.xinitrc')

    print("\n###zshrc")
    get_ipython().system('cp ~/Program/InstallTools/zsh/.zshrc ~/.zshrc')

    print("\n###qtile")
    get_ipython().system('mkdir -p ~/.config/qtile')
    get_ipython().system('cp ~/Program/InstallTools/qtile/config.py ~/.config/qtile/')

if __name__ == '__main__':
    main()
