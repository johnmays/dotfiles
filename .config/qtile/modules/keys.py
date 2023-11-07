from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
# terminal = "xfce4-terminal"
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),
    Key([mod, "shift"],
        "Left",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),
    Key([mod, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),
    Key([mod, "shift"],
        "Right",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "Up",
        lazy.layout.grow(),
        desc="Grow window"
        ),
    Key([mod, "control"],
        "Down",
        lazy.layout.shrink(),
        desc="Shrink window"
        ),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_colscreenumn_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
]
