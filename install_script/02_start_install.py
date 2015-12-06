#!/usr/bin/env python
# -*- coding: utf-8 -*-

### H27 Mar 16

import os, sys
import subprocess

SCRIPTDIR = os.path.dirname(os.path.abspath(__file__))
HOMEDIR = os.environ['HOME']
PKGFILE = os.path.join(SCRIPTDIR, 'pkglist')


#----- call_system() -----#
def call_system(cmd):
    splitted_cmd = cmd.split()
    subprocess.call(splitted_cmd)


#----- call_pacman() -----#
def call_pacman(pkg):
    cmd = "pacman -S {0} --needed --noconfirm".format(pkg)
    call_system(cmd)


#----- installPkg() -----#
def installPkg():
    # Full system update
    call_system("pacman -Syu --noconfirm")
    # Install packages
    pkglist = open(PKGFILE).readlines()
    for i in range(len(pkglist)):
        call_pacman(pkglist[i])


#----- main() -----#
def main():
    installPkg()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl+C -> END")

