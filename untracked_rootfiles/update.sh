# !/usr/bin/sh

# This script is for copying over the few rootfiles I am informally tracking to this directory

WALLPAPER_FROM_PATH="/usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png"
THEMES_FROM_PATH="/usr/share/themes/placeholder"

WALLPAPER_TO_PATH="~/untracked_rootfiles/usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png"
THEMES_TO_PATH="~/untracked_rootfiles/usr/share/themes/placeholder"

cp $WALLPAPER_FROM_PATH $WALLPAPER_TO_PATH
cp $THEMES_FROM_PATH $THEMES_TO_PATH