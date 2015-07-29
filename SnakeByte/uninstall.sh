#!/bin/bash

sudo echo "Start uninstall SnakeByte from your system..."

if [[ $? != '0' ]]
then
echo "This installation script must be run as root"
return 1
fi




way_share_file_folder="/usr/share/SnakeByte"
way_prog_file="/usr/bin/SnakeByte.py"
way_home_files_folder="$HOME/.SnakeByte/"
way_desktop_file="/usr/share/applications/SnakeByte.desktop"



if [[ -d /usr/share/SnakeByte/ ]]
then
  sudo rm -R ${way_share_file_folder}
fi

if [[ -f /usr/bin/SnakeByte.py ]]
then
  sudo rm ${way_prog_file}
fi

if [[ -f /usr/share/applications/SnakeByte.desktop ]]
then
  sudo rm ${way_desktop_file}
fi

echo "SnakeByte correctly removed from your system."
