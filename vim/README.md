
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

---

# Manuals

surround.vim
============

Surround.vim is all about "surroundings": parentheses, brackets, quotes,
XML tags, and more.  The plugin provides mappings to easily delete,
change and add such surroundings in pairs.

It's easiest to explain with examples.  Press `cs"'` inside

    "Hello world!"

to change it to

    'Hello world!'

Now press `cs'<q>` to change it to

    <q>Hello world!</q>

To go full circle, press `cst"` to get

    "Hello world!"

To remove the delimiters entirely, press `ds"`.

    Hello world!

Now with the cursor on "Hello", press `ysiw]` (`iw` is a text object).

    [Hello] world!

Let's make that braces and add some space (use `}` instead of `{` for no
space): `cs]{`

    { Hello } world!

Now wrap the entire line in parentheses with `yssb` or `yss)`.

    ({ Hello } world!)

Revert to the original text: `ds{ds)`

    Hello world!

Emphasize hello: `ysiw<em>`

    <em>Hello</em> world!

Finally, let's try out visual mode. Press a capital V (for linewise
visual mode) followed by `S<p class="important">`.

    <p class="important">
      <em>Hello</em> world!
    </p>

This plugin is very powerful for HTML and XML editing, a niche which
currently seems underfilled in Vim land.  (As opposed to HTML/XML
*inserting*, for which many plugins are available).  Adding, changing,
and removing pairs of tags simultaneously is a breeze.

The `.` command will work with `ds`, `cs`, and `yss` if you install
[repeat.vim](https://github.com/tpope/vim-repeat).




[1]: https://bradmontgomery.net/blog/vim-syntax-highlighting-for-apache-config-files/
[2]: https://www.fullstackpython.com/vim.html
[3]: https://github.com/VundleVim/Vundle.vim#quick-start 
