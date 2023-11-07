#!/usr/bin/sh

# This script is just for quickly updating the 
# package lists that are in my config repo

pacmanpath="$HOME/Projects/config_notes/pacman_packages.txt"
yaypath="$HOME/Projects/config_notes/yay_packages.txt"

echo updating pacman packages...
pacman -Qe > $pacmanpath
echo finished updating pacman

echo updating yay packages...
yay -Qe > $yaypath
echo finished updating yay