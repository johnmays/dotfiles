#!/usr/bin/sh

# This script is just for quickly updating the 
# package lists that are in my config repo

PACMAN_PATH="$HOME/Projects/config_notes/pacman_packages.txt"
YAY_PATH="$HOME/Projects/config_notes/yay_packages.txt"
CODE_EXTENSION_PATH="$HOME/Projects/config_notes/code_extensions.txt"

echo updating pacman packages...
pacman -Qe > $CODE_EXTENSION_PATH
echo finished updating pacman

echo updating yay packages...
yay -Qe > $YAY_PATH
echo finished updating yay

echo updating VSCode extensions...
code --list-extensions > $CODE_EXTENSION_PATH
echo finished updating code extensions