#!/usr/bin/sh

# This script is for quickly disconnecting from my
# bluetooth devices
if [ "$1" = "-h" ] || [ "$1" = "--help" ]
then
    echo "BT disconnection utility using bluez"
    echo
    echo "Options:"
    echo -e "\t-h, --help  Displays this help"
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

    echo "Which devices would you like to disconnect from?"
    for i in "${!DEVICES[@]}"; do
        printf "DEVICE: %s? [Y/n] " "${DEVICES[i]}"
        read INPUT_STR
        if [ "${INPUT_STR,,}" = "y" ]
        then
            printf "pairing: %s at %s\n" "${DEVICES[i]}" "${ADDRESSES[i]}"
            
            bluetoothctl power on
            bluetoothctl agent on
            # bluetoothctl scan on
            # bluetoothctl wait
            sleep 1
            bluetoothctl disconnect "${ADDRESSES[i]}"
        fi
    done

    bluetoothctl exit

    echo "Finished"
fi