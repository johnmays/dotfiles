#!/usr/bin/sh

# This script is just for quickly connecting to my
# bluetooth devices
if [ "$1" = "-h" ] || [ "$1" = "--help" ]
then
    echo "BT connection utility using bluez"
    echo
    echo "Options:"
    echo -e "\t-h, --help  Displays this help"
    echo -e "\t-i, --init  Pass if running script for first time after startup"
    echo
else
    DEVICES=(
    "Headphones (WHs)"
    "Mouse (MX)"
    )
    ADDRESSES=(
        "88:C9:E8:A1:A6:34"
        "placeholder"
    )

    if [ "$1" = "-i" ] || [ "$1" = "--init" ]
    then
        echo "Initializing..."
        sleep 0.5
        sudo systemctl start bluetooth
        sudo systemctl enable bluetooth
        systemctl status bluetooth
    fi

    echo "Which devices would you like to pair?"
    for i in "${!DEVICES[@]}"; do
        printf "DEVICE: %s? [Y/n] " "${DEVICES[i]}"
        read INPUT_STR
        if [ "${INPUT_STR,,}" = "y" ]
        then
            printf "pairing: %s at %s\n" "${DEVICES[i]}" "${ADDRESSES[i]}"
            
            bluetoothctl power on
            bluetoothctl agent on
            bluetoothctl default-agent
            # bluetoothctl scan on
            # bluetoothctl wait
            sleep 1
            bluetoothctl pair "${ADDRESSES[i]}"
            bluetoothctl connect "${ADDRESSES[i]}"
        fi
    done

    bluetoothctl exit

    echo "Finished"
fi