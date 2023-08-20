# linux_usb_wifi_drv_finder
Determine the list of USB WiFi chipsets with already installed drivers


Usage:

1. First, run `list_vid_pid`. It will loop over installed drivers and extract the list of VID:PID identifiers of the USB devices they support.
1. Then, download [http://www.linux-usb.org/usb.ids]() and delete everything after the list of known VID:PID.
1. 
