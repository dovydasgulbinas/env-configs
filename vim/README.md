
# Enable highlighting for files with no extensions
    
0. Create conf dir: `mkdir $HOME/.vim/`
1. Create file: `touch $HOME/.vim/filetype.vim`
2. Add [highlight support][1]: `echo "au BufNewFile,BufRead $HOME/.vifm/* setf vim" >> $HOME/.vim/filetype.vim`
3. Add your vim conf [file][2]: `cp ./basic.vimrc $HOME/.vimrc` 


[1]: https://bradmontgomery.net/blog/vim-syntax-highlighting-for-apache-config-files/
[2]: https://www.fullstackpython.com/vim.html
