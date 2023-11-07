from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os
from modules.colors import *
from modules.custom_widgets import custom_groupbox, custom_volume

pad_length = 6

screens = [
    Screen(
        wallpaper="~/.config/qtile/background.png",
        top=bar.Bar(
            [
                custom_groupbox.GroupBox(
                    highlight_method = 'block',
                    this_screen_border = offwhite,
                    this_current_screen_border=blue,
                    active = offwhite,
                    inactive = gray,
                    inactive_highlight = darkergray,
                    background=darkergray,
                    disable_drag=True,
                    visible_groups = ['1', '2', '3', '4', '5'],
                    margin = 3,
                    spacing = pad_length,
                    rounded = False,
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
                    background=darkgray
                ),
                custom_volume.Volume(
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
                widget.Battery(
                    battery = 0,
                    format = "BAT0: {percent:2.0%},",
                    show_short_text = False,
                    foreground = offwhite
                ),
                widget.Battery(
                    battery = 1,
                    format = "BAT1: {percent:2.0%}",
                    show_short_text = False,
                    foreground = offwhite
                ),
                # widget.Sep(padding=pad_length, linewidth=0, background=darkgray),
                # widget.Bluetooth(),
                # widget.Wlan(),
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
            48,  # height in px
            background=darkgray  # background color
        ) ),
]
