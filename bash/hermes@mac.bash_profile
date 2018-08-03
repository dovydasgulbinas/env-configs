export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_TYPE=en_US.UTF-8
export LANGUAGE=en_US.UTF-8

export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'
export GREP_OPTIONS='--color=always'
export GREP_COLOR='00;38;5;157'
export TERM=xterm-256color
export ANACONDA_DIR="$HOME/anaconda"
export PYTHONDONTWRITEBYTECODE=1  # ENABLE IN PROD ENVS
export EDITOR=vim
# use vi keybindings
set -o vi

# Path Exports
export PATH="$ANACONDA_DIR/bin:$PATH"
export PATH=$SCRIPTS_DIR:$PATH
export PATH=~/bin:$PATH

alias mac-home="cd /root/Desktop/Parallels\ Shared\ Folders/Home/whacking"

# My Non Sys vars
export SYNC_DIR="$HOME/Sync"
export NB_DIR="$SYNC_DIR/notebook"
export BLOG_DIR="$SYNC_DIR/diy/blog"
export DIY_DIR="$SYNC_DIR/diy"
export FSONG_FPATH="$SYNC_DIR/logs/to-listen.txt"

export SCRIPTS_DIR="$HOME/diy/env-configs/scripts"
export PROJECT_DIR="$HOME/Projects"
