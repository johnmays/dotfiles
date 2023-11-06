## qtile:
- `qtile cmd-obj -o cmd -f restart` refresh config from local files
- `qtile cmd-obj -o cmd -f reload_config` same, but if you're using git to version the config
## pacman:
- `sudo pacman -Syu <package>` install and update
- `sudo pacman -Rs <package>` uninstall and weed out dependencies only used by `<package>`
- `sudo pacman -Ss "<string>"` search for packages