#!/usr/bin/sh

# This script is just for quickly connecting to my
# bluetooth devices

DEVICES=(
    "Headphones (WHs)"
    "Mouse (MX)"
)
ADDRESSES=(
    "88:C9:E8:A1:A6:34"
    "placeholder"
)

# sudo systemctl start bluetooth
# sudo systemctl enable bluetooth
# systemctl status bluetooth

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
        bluetoothctl scan on
        # bluetoothctl wait
        bluetoothctl pair "${ADDRESSES[i]}"
        bluetoothctl connect "${ADDRESSES[i]}"
    fi
done

bluetoothctl exit

echo "Finished"
