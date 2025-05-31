#!/bin/bash

batteryPerc=$(cat /sys/class/power_supply/BAT0/capacity)
batteryStatus=$(cat /sys/class/power_supply/BAT0/status)

if [ "$batteryStatus" = "Charging" ] || [ "$batteryStatus" = "Full" ] ; then
	icon="󰂄"
else
	icon="󰂀"
fi

echo "$icon $batteryPerc%"

