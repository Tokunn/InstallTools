xrandr --setprovideroutputsource modesetting NVIDIA-0
#xrandr --auto
xrandr --output VGA-1 --auto --output HDMI-1 --auto --left-of VGA-1
#xrandr --output VGA-1-1 --auto --output LVDS-1-1 --auto --left-of VGA-1-1
#xrandr --output HDMI-1-1 --auto --output LVDS-1-1 --auto --left-of HDMI-1-1
#xrandr --output LVDS-1-1 --auto
xmodmap -e "keycode 49 = Super_L" -e "add mod4 = Super_L"
exec awesome
#exec qtile
