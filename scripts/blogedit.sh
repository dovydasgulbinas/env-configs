#!/bin/bash
blogdir="$BLOG_DIR"

cd $blogdir
tmux new-session -s 'blog' -d "vifm $blogdir"
tmux new-window "$SCRIPTS_DIR/blogserve.sh" 
tmux split-window -v 
tmux -2 attach-session -d

# [source]: (https://stackoverflow.com/questions/5609192/how-to-set-up-tmux-so-that-it-starts-up-with-specified-windows-opened#5752901)
