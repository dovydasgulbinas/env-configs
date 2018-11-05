herver='hermes@namas.duckdns.org'
media='media@namas.duckdns.org'
tv='osmc@namas.duckdns.org'

alias belly="ssh pi@berry.local"
alias berry="ssh pi@namas.duckdns.org"
alias warsaw="ssh pi@213.159.56.188"
alias loreta="ssh osmc@loreta.local"
alias hass="ssh root@hassio.local"
alias hass-host="ssh root@hassio.local -p 22222"
alias kali="ssh hermes@192.168.0.9"
alias tv="ssh $tv -p 55522"
alias media="ssh $media"
alias herver="ssh $herver"

pldir="$MUSIC_MOUNT_DIR/__playlists__"

pfw(){
browser http://localhost:$2
ssh $1 -L $2:${3:-localhost}:$2
}

alias tv-tr="open http://localhost:9091 && ssh osmc@namas.duckdns.org -p 55522 -L 9091:127.0.0.1:9091"
alias tv-son="open http://localhost:8989 && ssh osmc@namas.duckdns.org -p 55522 -L 8989:127.0.0.1:8989"
alias tv-ebot="open http://localhost:8081 && ssh osmc@namas.duckdns.org -p 55522 -L 8081:192.168.0.7:8081"
alias tv-hole="open http://localhost:9999 && ssh osmc@namas.duckdns.org -p 55522 -L 9999:192.168.0.105:8111"
alias hass-term="open https://localhost:7681 && ssh osmc@namas.duckdns.org -p 55522 -L 7681:hassio.local:7681"
alias hass-loc="open https://localhost:8123 && ssh osmc@namas.duckdns.org -p 55522 -L 8123:hassio.local:8123"



alias mmpv="mpv --snap-window --shuffle --autofit-larger='10%' --geometry='-10-10' --gapless-audio"
#alias mumount="umount $MUSIC_MOUNT_DIR && sshfs media@namas.duckdns.org:/media/raid/media/beets-music $MUSIC_MOUNT_DIR"
alias mumount="sshfs -o reconnect  media@namas.duckdns.org:/media/raid/media/beets-music $MUSIC_MOUNT_DIR"
alias umumount="sudo diskutil umount force $MUSIC_MOUNT_DIR"


alias mpvnova='mpv --no-video'
alias mpvshuf='mpvnova --shuffle --loop-playlist=inf'
alias mpvp='mpvshuf --playlist'

playcurrentdir() {
  mpvp <(find "$PWD" -type f -follow)
}
alias pcd='playcurrentdir'

alias mupl='mmpv --loop-playlist=inf --no-video --playlist'

# alias slink='streamlink   --stream-url "https://www.twitch.tv/faceittv" best'

alias hr-tr="pfw $herver 9091"
alias hr-znet="pfw $herver 43110 192.168.0.8"
alias hr-frss="pfw $herver 8619 192.168.0.8"
alias hr-beets="pfw $media 8337"
alias hr-br="pfw $media 5000"
alias hr-hass="pfw $herver 8123 192.168.0.105"
alias hr-router='$herver -L 8080:192.168.0.1:80'
alias hr-socks="ssh -D 8280 -f -C -q -N hermes@namas.duckdns.org"

# conf section
alias aconf="vim ~/.bash_aliases"

# go section
alias cass="cat $HOME/.ssh/id_rsa.pub"
alias nb="cd $NB_DIR"
alias nbs="$NB_DIR/nb-find.sh"
alias bl="cd $BLOG_DIR"
alias diy="cd $DIY_DIR"
alias ec="cd $ENV_CONFIGS_DIR"
alias pj="cd $PROJECTS_DIR"
alias scripts="cd $SCRIPTS_DIR"
alias dep="cd /Users/hermes/Projects/ldap-project/deployment"
alias goals="$NB_DIR/Growth/goal-pack/g.sh"

alias yc="$SYNC_DIR/yt-cache"
alias t="todo.sh"
alias vt="$EDITOR $TODO_FILE"
alias qn="$EDITOR $NB_DIR/Loose/QuickNote.md"
alias nbu="$EDITOR $HOME/.newsboat/urls"
alias streamlinkit="streamlink https://www.twitch.tv/food --player-passthrough rtmp -p mpv"


if [ -f ~/.bash_aliases_mac ]; then
    . ~/.bash_aliases_mac
  fi


# [1]: https://stackoverflow.com/questions/27384725/ssh-x-warning-untrusted-x11-forwarding-setup-failed-xauth-key-data-not-gener
