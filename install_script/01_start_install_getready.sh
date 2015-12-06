#!/usr/bin/env sh

systemctl enable dhcpcd.service

pacman -Syu --noconfirm --needed
pacman -S git python2 python3 --noconfirm --needed

./02_start_install.py
