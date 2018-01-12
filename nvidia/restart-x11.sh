#!/bin/bash

dfile="$(cat /etc/X11/default-display-manager)"

dispdaemon="$(basename $dfile)"
printf "Dispday daemon executable: $dfile\n"
printf "Default dispday daemon is: $dispdaemon\n"

read -p "Do you wish to restart the dispday daemon (y/n)?" choice
case "$choice" in 
  y|Y ) echo "yes" && systemctl restart "$dispdaemon";;
  n|N ) echo "no";;
  * ) echo "invalid";;
esac
