#!/usr/bin/env python

import sys, os
import subprocess

gui_config = """
Section "InputClass"
    Identifier      "Keyboard Defaults"
    MatchIsKeyboard "yes"
    Option         "XkbLayout" "jp"
EndSection
"""
lxde = """
exec startlxde
"""
custom_bashrc = """
setfont Lat2-Terminus16
"""

def call_system(cmd):
    splitted_cmd = cmd.split()
    subprocess.call(splitted_cmd)

def install(soft):
    cmd = "pacman -S {0} --noconfirm".format(soft)
    call_system(cmd)

def main():

    print("#1 System update")
    call_system("pacman -Syu --noconfirm")

    print("#2 Install")
    software = ['vim', 'tmux', 'sudo', 'visudo', 'traceroute', 'nmap', 'gdb', 'wireshark-gtk', 'net-tools', 'wget', 'otf-ipafont', 'python2-pyserial', 'vim-systemd', 'python2-pygame', 'openssh', 'acpi']
    for i in range(len(software)):
        print(software[i])
        install(software[i])
    call_system("visudo")

    print("#3 Add New User")
    print("Do you want to add new users? [Y/n]")
    yorn = input('-->')
    if ((yorn == 'y') or (yorn == 'Y')):
        print("Type usernaem")
        username = input('-->')
        call_system("useradd -m -g users -G wheel -s /bin/bash {0}".format(username))
        print("Set password")
        call_system("passwd {0}".format(username))

    print("#4 Install GUI")
    print("Do you want to install GUI? [Y/n]")
    yorn = input('-->')
    if ((yorn == 'y') or (yorn == 'Y')):
        software = ['xorg-server', 'xorg-server-utils', 'xorg-xinit', 'mesa', 'xf86-video-fbdev', 'xf86-input-synaptics', 'lxde', 'awesome', 'chromium']
        for i in range(len(software)):
            print(software[i])
            install(software[i])
        f = open('/etc/X11/xorg.conf.d/10-keyboard.conf', 'w')
        f.write(gui_config)
        f.close()
        print("Type username")
        username = input('-->')
        f = open('/home/{0}/.xinitrc'.format(username), 'w')
        f.write(lxde)
        f.close()

    print("#5 Custom .bashrc")
    print("Do you want to custom .bashrc? [Y/n]")
    yorn = input('-->')
    if ((yorn == 'y') or (yorn == 'Y')):
        print("Type usernaem")
        username = input('-->')
        f = open('/home/{0}/.bashrc'.format(username), 'a')
        f.write(custom_bashrc)
        f.close()

    print("#6 Custom /etc/fstab")
    print("Do you want to custom /etc/fstab? [Y/n]")
    yorn = input('-->')
    if ((yorn == 'y') or (yorn == 'Y')):
        pass

    print("Conplete!")
    print("Please install yaourt")
    print("Please install archassault")


if __name__ == '__main__':
    main()
