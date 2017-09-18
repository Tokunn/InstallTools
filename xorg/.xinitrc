xrandr --setprovideroutputsource modesetting NVIDIA-0
xrandr --auto
xrandr --output HDMI-1-1 --auto --output LVDS-1-1 --auto --left-of HDMI-1-1
exec awesome
