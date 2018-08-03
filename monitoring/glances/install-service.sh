#!/bin/bash


fnm="${1%.*}"
snm="$fnm.service"

echo "Copying files: $snm"

cp "./$snm" /etc/systemd/system

systemctl daemon-reload
systemctl start $snm 
systemctl enable $snm
systemctl status $snm
