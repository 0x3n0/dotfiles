#!/bin/sh

## Start

dwmblocks &

picom -CGb &

xrdb .Xresources &

nitrogen --restore &

## resolution layout
#xrandr --output LVDS1 --scale 1.25x1.25 &

exec dwm
