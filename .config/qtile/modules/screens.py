from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

darkestgray = "#171b1c"
darkergray = "#24282a"
darkgray = "#3c4549"
gray = "#555c61"
lightgray = "#adafb1"
offwhite = "#c6c7c8"
darkblue = "#0d4662"
blue = "#07628f"
lightblue = "#017dbb"
red = "#bb4542"
orange = "#bb6742"
yellow = "#bc955c"

pad_length = 6

screens = [
    Screen(
        wallpaper="~/.config/qtile/background.png",
        top=bar.Bar(
            [   widget.Sep(padding=pad_length, linewidth=0, background=darkergray),
                widget.GroupBox(
                                highlight_method='block',
                                this_screen_border="#00ff00",
                                this_current_screen_border=blue,
                                active=offwhite,
                                inactive=gray,
                                background=darkergray,
                                disable_drag=False
                ),
                widget.Spacer(length=5),
                widget.WindowName(foreground=lightblue,fmt='{}'),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground=offwhite,
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    background="#2f343f"),
                # widget.Systray(icon_size = 20),
                widget.Volume(
                    foreground=offwhite,
                    background=darkgray
                ),
                widget.Sep(padding=pad_length, linewidth=0, background=darkgray),
                widget.Sep(padding=pad_length, linewidth=0, background=darkergray),
                widget.Clock(format='%m/%d/%Y %a %I:%M %p',
                             background=darkergray,
                             foreground=offwhite
                ),
                widget.Sep(padding=pad_length, linewidth=0, background=darkergray),
                widget.Sep(padding=pad_length, linewidth=0, background=darkgray),
                widget.TextBox( # Power button
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=red
                ),
                widget.Sep(padding=pad_length, linewidth=0, background=darkgray)
            ],
            40,  # height in px
            background=darkgray  # background color
        ) ),
]
