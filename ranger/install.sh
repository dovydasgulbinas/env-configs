#!/bin/bash

make_backup(){

    if [ -f $1 ] || [ -d $1 ] || [ -h $1 ]; then
        mv $1 "$1.$(date +%s%3N).bak"
    fi
}

make_symlink(){
    ln -s "$1" "$2"
    ls -alth "$dst"
}


src="$ENV_CONFIG_DIR/ranger"  # place where you keep your confs
dst="$HOME/.config/ranger"  # e.g. ~/.config/ranger

make_backup $dst
make_symlink $src $dst
