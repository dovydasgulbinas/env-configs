alias ringbell="echo -e '\a'" # https://superuser.com/questions/598783/play-sound-on-mac-terminal

if [ "$(uname)" = 'Linux' ]; then
    export OS='Linux'
    alias notifier='notify-send' # streamlines notifiers for all systems

# MAC users
elif [ "$(uname)" = 'Darwin' ]; then
    export HOSTNAME="$HOST" 
    export OS='Darwin'
    alias sed='gsed' # 
    alias browser="/usr/bin/open -a /Applications/Firefox.app"
    alias date='gdate' # installed with `brew install coreutils` https://archive.fo/Vq2ZA
    alias notifier='terminal-notifier' # streamlines notifiers for all systems
    alias paster='pbpaste'
    alias copier='pbcopy'
    alias cal='gcal --starting-day=1' # `brew install gcal`

else
    echo "Windows & BSD BTFO!";
fi

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_TYPE=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export SSH_KEY_PATH="$HOME/.ssh/rsa_id"
export ARCHFLAGS="-arch x86_64"

# export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'
# export GREP_OPTIONS='--color=always'
export GREP_COLOR='00;38;5;157'
export TERM=xterm-256color
export ANACONDA_DIR="$HOME/anaconda"
export PYTHONDONTWRITEBYTECODE=1  # ENABLE IN PROD ENVS


export EDITOR='vim'
export TERM_FILE_MANAGER='ranger'
# Preferred editor for local and remote sessions
# if [ -n $SSH_CONNECTION ]; then
#   export EDITOR='vim'
# else
#   export EDITOR='vim'
# fi 


# use vi keybindings
set -o vi


# alias mac-home="cd /root/Desktop/Parallels\ Shared\ Folders/Home/whacking"

# My Non Sys vars
export BOOKS_DIR="$HOME/Books"
export DIY_DIR="$HOME/diy"
export SYNC_DIR="$HOME/Sync"
export NB_DIR="$SYNC_DIR/notebook"
export STICKIES_DIR="$NB_DIR/Loose/stickies"
export SCREENSHOTS_DIR="$SYNC_DIR/screen-shots"
export BLOG_DIR="$DIY_DIR/blog"
# MUSIC
export BEETS_PARTIAL="beets-music"
export FSONG_FPATH="$SYNC_DIR/logs/beets-favs.m3u"
export MUSIC_MOUNT_DIR="$HOME/Music/$BEETS_PARTIAL"

export ENV_CONFIG_DIR="$DIY_DIR/env-configs"
export SCRIPTS_DIR="$ENV_CONFIG_DIR/scripts"
export BASH_MODULES_DIR="$HOME/.bash_modules"
export PROJECTS_DIR="$HOME/Projects"
export TODO_DIR="$SYNC_DIR/todo"
export TODO_FILE="$TODO_DIR/todo.txt"
export QUICK_NOTE_DIR="$NB_DIR/Loose/QuickNote.md"
export DAILY_LOG_DIR="$NB_DIR/Health/daily-logs"
export GOALS_DIR="$NB_DIR/Growth/goal-pack"
export GOALS_FILE="$GOALS_DIR/goals-main.md"
# export TODO_DIR="$NB_DIR/Growth/goal-pack/todo.txt"

# Path Exports
# export PATH="$ANACONDA_DIR/bin:$PATH"
export PATH="$SCRIPTS_DIR:$PATH"
export PATH="$BASH_MODULES_DIR:$PATH"
export PATH="$HOME/bin:$PATH"
