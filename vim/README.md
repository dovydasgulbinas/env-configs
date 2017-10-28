
# Enable highlighting for files with no extensions
    
0. Create conf dir: `mkdir $HOME/.vim/`
1. Create file: `touch $HOME/.vim/filetype.vim`
2. Add [highlight support][1]: `echo "au BufNewFile,BufRead $HOME/.vifm/* setf vim" >> $HOME/.vim/filetype.vim`
3. Add your vim conf [file][2]: `cp ./basic.vimrc $HOME/.vimrc` 

# Symlink Vim config 

0. Go Home: cd ~ 
1. Create link e.g. to vimrc-mac: `ln -s "{path_to_file}/vimrc-mac .vimrc"`

# Install [Vundle][3] plugin manager

`git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim`



[1]: https://bradmontgomery.net/blog/vim-syntax-highlighting-for-apache-config-files/
[2]: https://www.fullstackpython.com/vim.html
[3]: https://github.com/VundleVim/Vundle.vim#quick-start 
