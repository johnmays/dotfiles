from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen
from modules.keys import terminal
from libqtile.lazy import lazy
import os
from modules.colors import *
from modules.custom_widgets import custom_groupbox, custom_volume

pad_length = 6

screens = [
    Screen(
        wallpaper="~/assets/backgrounds/background_02_colors.png",
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
                # widget.CheckUpdates(
                #     update_interval=1800,
                #     distro="Arch_yay",
                #     display_format="{updates} Updates",
                #     foreground=offwhite
                # ),
                # THIS IS WHERE THE ALIGNMENT SEPARATION IS
                custom_volume.Volume(
                    foreground=offwhite,
                    background=darkgray
                ),
                # widget.Mpris2(),
                # widget.TextBox( # RW button
                #     text='⏪',
                #     mouse_callbacks= {
                #         'Button1':
                #         lambda: lazy.widget["mpris2"].previous()
                #     },
                #     foreground=offwhite,
                #     background=darkgray
                # ),
                # widget.TextBox( # Pause buttons
                #     text='⏸',
                #     mouse_callbacks= {
                #         'Button1':
                #         lambda: lazy.widget["mpris2"].play_pause()
                #     },
                #     foreground=offwhite,
                #     background=darkgray
                # ),
                # widget.TextBox( # FFW button
                #     text='⏩',
                #     mouse_callbacks= {
                #         'Button1':
                #         lambda: lazy.widget["mpris2"].next()
                #     },
                #     foreground=offwhite,
                #     background=darkgray
                # ),
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
                    format = "{percent:2.0%},",
                    show_short_text = False,
                    foreground = offwhite,
                    low_foreground = red,
                    low_percwntage = 0.1
                ),
                widget.Battery(
                    battery = 1,
                    format = "{percent:2.0%}",
                    show_short_text = False,
                    foreground = offwhite,
                    low_foreground = red,
                    low_percwntage = 0.1
                ),
                # widget.Sep(padding=pad_length, linewidth=0, background=darkgray),
                # widget.Bluetooth(),
                # widget.Wlan(),
                widget.Sep(padding=pad_length, linewidth=0, background=darkgray),
                widget.Sep(padding=pad_length, linewidth=0, background=darkergray),
                widget.TextBox( # Power button
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=offwhite,
                    background=darkergray
                ),
                widget.Sep(padding=pad_length, linewidth=0, background=darkergray)
            ],
            48,  # height in px
            background=darkgray  # background color
        ) ),
]
