#!/bin/bash

herver='hermes@namas.duckdns.org'
media='media@namas.duckdns.org'

alias belly="ssh pi@berry.local"
alias berry="ssh pi@namas.duckdns.org"
alias warsaw="ssh pi@213.159.56.188"
alias loreta="ssh osmc@loreta.local"
alias hass="ssh root@hassio.local"
alias hass-host="ssh root@hassio.local -p 22222"
alias tv="ssh osmc@namas.duckdns.org -p 55522"
alias kali="ssh hermes@192.168.0.9"
alias kalir="ssh -p 4422 -v hermes@namas.duckdns.org"

pfw(){
"echo http://localhost:$1 && ssh $2 -L $1:127.0.0.1:$1"
}

alias tv-tr="open http://localhost:9091 && ssh osmc@namas.duckdns.org -p 55522 -L 9091:127.0.0.1:9091"
alias tv-son="open http://localhost:8989 && ssh osmc@namas.duckdns.org -p 55522 -L 8989:127.0.0.1:8989"
alias tv-rad="open http://localhost:7878 && ssh osmc@namas.duckdns.org -p 55522 -L 7878:127.0.0.1:7878"
alias tv-jack="open http://localhost:9117 && ssh osmc@namas.duckdns.org -p 55522 -L 9117:127.0.0.1:9117"
alias tv-router="open http://localhost:8080 && ssh osmc@namas.duckdns.org -p 55522 -L 8080:192.168.0.1:80"
alias tv-ebot="open http://localhost:8081 && ssh osmc@namas.duckdns.org -p 55522 -L 8081:192.168.0.7:8081"
alias tv-hole="open http://localhost:9999 && ssh osmc@namas.duckdns.org -p 55522 -L 9999:192.168.0.105:8111"
alias hass-term="open https://localhost:7681 && ssh osmc@namas.duckdns.org -p 55522 -L 7681:hassio.local:7681"
alias hass-loc="open https://localhost:8123 && ssh osmc@namas.duckdns.org -p 55522 -L 8123:hassio.local:8123"

confdir="$HOME/diy/env-configs"
shellrc="$HOME/.bashrc"
shellalias="$HOME/.bash_aliases"


alias def="/usr/bin/sdcv"
alias open='nautilus'
alias delet="shred -vuz"


# conf utils
alias sconf="vim $shellrc"
alias aconf="vim $shellalias"
alias sfind="cat $shellrc | grep"
alias afind="cat $shellalias | grep"


# dir based
alias diy="cd $HOME/diy"
alias cdir="cd $confdir"


# music

alias mkfav="echo $PWD > $HOME/.favdir"
alias fav="cd $(cat $HOME/.favdir)"
alias fsong="mpc | head -n 1 >> $HOME/Desktop/to-listen.txt && tail -n 5 $HOME/Desktop/to-listen.txt"

# notes
alias markr="flatpak run com.github.fabiocolacio.marker"


# https://wiki.archlinux.org/index.php/Sdcv
