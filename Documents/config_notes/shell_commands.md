p## qtile:
- `qtile cmd-obj -o cmd -f restart` refresh config from local files
- _super + ctrl + r_ also reloads qtile
- `qtile cmd-obj -o cmd -f reload_config` same, but if you're using git to version the config
## pacman:
- `sudo pacman -Syu <package>` install and update
- `sudo pacman -Rs <package>` uninstall and weed out dependencies only used by `<package>`
- `sudo pacman -Ss "<string>"` search for packages
## yay:
- similar arg structure to pacman
## cfg
- `cfg add -u` adds all tracked, un-staged files