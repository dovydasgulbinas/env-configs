# https://wiki.archlinux.org/index.php/Sdcv

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
