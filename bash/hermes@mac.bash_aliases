herver="ssh hermes@namas.duckdns.org"

alias media="ssh media@namas.duckdns.org"
alias belly="ssh pi@berry.local"
alias berry="ssh pi@namas.duckdns.org"
alias warsaw="ssh pi@213.159.56.188"
alias herver="$herver"
alias loreta="ssh osmc@loreta.local"
alias hass="ssh root@hassio.local"
alias hass-host="ssh root@hassio.local -p 22222"
alias tv="ssh osmc@namas.duckdns.org -p 55522"
alias kali="ssh hermes@192.168.0.9"
alias kalir="ssh -p 4422 -v hermes@namas.duckdns.org"

pfw(){
"open http://localhost:$1 && $2 -L $1:127.0.0.1:$1"
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

alias herver-tr='pfw 9091 $herver'
alias herver-router='$herver -L 8080:192.168.0.1:80'

alias socks="ssh -D 8280 -f -C -q -N hermes@namas.duckdns.org"
alias mumount="sshfs media@namas.duckdns.org:/media/raid/media/music ~/Music/sshfs-music"

# conf section
alias aconf="vim ~/.bash_aliases"

# go section
alias cass="cat $HOME/.ssh/id_rsa.pub"
# alias nb="cd $NB_DIR"
alias b="cd $BLOG_DIR"
alias diy="cd $DIY_DIR"
alias dep="cd /Users/hermes/Projects/ldap-project/deployment"
alias p="cd $PROJECT_DIR"
alias scripts="cd $SCRIPTS_DIR"
alias goals="$NB_DIR/Growth/goal-pack/g.sh"
alias nbs="$NB_DIR/nb-find.sh"



