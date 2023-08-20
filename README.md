# linux_usb_wifi_drv_finder
Determine the list of USB WiFi chipsets with already installed drivers


Usage:

1. First, run `./list_vid_pid` (prior to that, `chmod u+x list_vid_pid` might be needed).
   It will loop over installed drivers and extract the list of VID:PID identifiers of the USB devices they support.
1. Then, download [http://www.linux-usb.org/usb.ids]() and delete everything after the list of known VID:PID.
1. Run it as ` python process_vid_pid.py > known_vid_pid`
1. Find chipset names: `grep -f usb_wireless_vid_pid.txt known_vid_pid | python RT.py | sort | uniq`
