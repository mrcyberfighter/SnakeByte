#!/bin/bash


sudo echo 'Start installation from the program SnakeByte...'
if [[ $? != '0' ]]
then
echo "This installation script must be run as root"
return 1
fi

# Check if module pygame is installed on your system.
python -c 'import pygame'
if [[ $? != 0 ]] ; then
  echo "SnakeByte require pygame python module"
  echo "Install the package python-pygame and retry installation."
  return 1
fi


#Define the pathes for the icon and the programm files
way_icon="$PWD/Icon/SnakeByte_icon.png"
way_prog="$PWD/Source/SnakeByte.py"
way_icon_dest="/usr/share/SnakeByte/SnakeByte_icon.png"
way_prog_dest="/usr/bin/SnakeByte.py"
way_read_me="$PWD/README/README.txt"
way_license="$PWD/License/license.txt"

if [[ ! -d "/usr/share/SnakeByte/" ]]
then

sudo echo "Make directory for programm files..."

sudo mkdir "/usr/share/SnakeByte/"

sudo mkdir "/usr/share/SnakeByte/Anim"

sudo mkdir "/usr/share/SnakeByte/Highscores/"

sudo mkdir "/usr/share/SnakeByte/Levels/"

sudo mkdir "/usr/share/SnakeByte/Icon/"

sudo mkdir "/usr/share/SnakeByte/Sound/"

sudo mkdir "/usr/share/SnakeByte/README/"

sudo mkdir "/usr/share/SnakeByte/License/"


fi

echo "Copy files needed from the programm..."

function copy_files() {

   if [[ -d "$2" ]]
   then

     echo "Copy files..."
     echo "from: $1"
     echo "To  : $2"
     echo
     sudo cp -R "$1"* "$2"

   else

     echo "$2 exist !"
     echo "Overwrite datas..."
     echo
     sudo cp -R "$1"* "$2"

   fi
}

copy_files  "$PWD/Anim/"          "/usr/share/SnakeByte/Anim/"
copy_files  "$PWD/Highscores/"    "/usr/share/SnakeByte/Highscores/"
copy_files  "$PWD/Levels/"        "/usr/share/SnakeByte/Levels/"
copy_files  "$PWD/Icon/"          "/usr/share/SnakeByte/Icon/"
copy_files  "$PWD/Sound/"         "/usr/share/SnakeByte/Sound/"

copy_files  "$PWD/README/"        "/usr/share/SnakeByte/README/"
copy_files  "$PWD/License/"       "/usr/share/SnakeByte/License/"

if [[ -d /usr/share/SnakeByte/Highscores/ ]]
then

  sudo chmod -R a+wx /usr/share/SnakeByte/Highscores/
fi

if [[ -d /usr/share/SnakeByte/Sound/ ]]
then

  sudo chmod -R go+rx /usr/share/SnakeByte/Sound/
fi

#Create an directory for SnakeByte to copy the needed files.
sudo cp ${way_prog} ${way_prog_dest}
sudo chmod a+x ${way_prog_dest}





echo 'Start shortcut creation'

if [[ -d /usr/share/applications && ! -f /usr/share/applications/SnakeByte.desktop ]]
then

  sudo cp "$PWD/Desktop/SnakeByte.desktop" /usr/share/applications/SnakeByte.desktop

else

  echo "Cannot create dekstop shortcut:"
  echo "No folder: /usr/share/applications"
  echo

fi



#You can remove the decrompressed SnakeByte directory now.
echo 'SnakeByte installation successfull'

