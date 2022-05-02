# PI Robot

* Robot - Gets commands, runs them
* GUI - Window to Control the robot

![GUI](./gui.png)

# Install

Require:
* Venv (Simon Only)
    * python3 -m venv build_virtual_env
    * Makes a virtual folder called build_virtual_env
* sudo apt-get install python3-tk
* cd GUI
* pip install -r requirements.txt
* sudo apt-get install i2c-tools
* sudo apt-get install python3-smbus

# Patch

* cd Patch
* sudo sh ./patch_for_bullseye.sh
* sudo nano /boot/config.txt
    * Place # before - > camera_auto_detect=1
    * Add f in to -> dtoverlay=vc4-kms-v3d -> dtoverlay=vc4-fkms-v3d
    * Add  
        * hdmi_force_hotplug=1
        * hdmi_ignore_edid=0xa5000080
        * hdmi_group=2
        * hdmi_mode=82
    * Ctrl+O
    * Ctrl+X
* sh ./build.sh


# Run

* cd GUI 
* python3 main.py

* cd Robot
* python3 main.py
