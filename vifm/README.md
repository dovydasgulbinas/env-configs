# Installation of vifm config

## In general 

```
# Add color support for terminal (bash)
echo "export TERM=xterm-256color" >> "$HOME/.bashrc"

# For zsh
echo "export TERM=xterm-256color" >> "$HOME/.zshrc"

# create vifm directories (OS X)
mkdir -p $HOME/.config/vifm/
mkdir -p $HOME/.config/vifm/colors/
mkdir -p $HOME/.config/vifm/scripts/

# create vifm directories (Ubuntu)
mkdir -p $HOME/.vifm/colors/
mkdir -p $HOME/.vifm/scripts/

# copy config on local machine
cp ./vifm-homebrew/vifmrc "$HOME/.config/vifm/" 


# if you want to do it on remote machine (copies file to clipboard MacOS only) 
cat ./vifm-homebrew/vifmrc | pbcopy
```



https://vifm.info/cheatsheets.shtml

# File Structure of Debian

```
# tree /usr/share/vifm

├── vifm-help.txt
├── vifmrc
├── vim
│   ├── autoload
│   │   └── vifm
│   │       └── edit.vim
│   ├── doc
│   │   ├── tags
│   │   └── vifm-plugin.txt
│   ├── ftdetect
│   │   ├── vifm-rename.vim
│   │   └── vifm.vim
│   ├── ftplugin
│   │   ├── mail_vifm.vim
│   │   ├── vifm-cmdedit.vim
│   │   ├── vifm-edit.vim
│   │   ├── vifm-rename.vim
│   │   └── vifm.vim
│   ├── plugin
│   │   └── vifm.vim
│   └── syntax
│       └── vifm.vim
└── vim-doc
    └── doc
        ├── tags
        └── vifm-app.txt
```

# File Structure of MacOS homebrew vifm=0.9
```
tree /usr/local/Cellar/vifm/0.9/share

/usr/local/Cellar/vifm/0.9/share
├── applications
│   └── vifm.desktop
├── bash-completion
│   └── completions
│       └── vifm
├── doc
│   └── vifm
│       ├── AUTHORS
│       ├── BUGS
│       ├── COPYING
│       ├── ChangeLog
│       ├── FAQ
│       ├── INSTALL
│       ├── NEWS
│       ├── README
│       └── TODO
├── man
│   └── man1
│       ├── vifm-convert-dircolors.1
│       ├── vifm-pause.1
│       ├── vifm-screen-split.1
│       └── vifm.1
├── pixmaps
│   └── vifm.png
├── vifm
│   ├── colors
│   │   ├── astrell-root.vifm
│   │   ├── astrell-user.vifm
│   │   ├── dmilith-root.vifm
│   │   ├── dmilith-user.vifm
│   │   ├── istib-solarized-dark.vifm
│   │   ├── juef-zenburn.vifm
│   │   └── reicheltd-light.vifm
│   ├── vifm-help.txt
│   ├── vifmrc
│   ├── vifmrc-osx
│   ├── vim
│   │   ├── autoload
│   │   │   └── vifm
│   │   │       └── edit.vim
│   │   ├── doc
│   │   │   ├── tags
│   │   │   └── vifm-plugin.txt
│   │   ├── ftdetect
│   │   │   ├── vifm-rename.vim
│   │   │   └── vifm.vim
│   │   ├── ftplugin
│   │   │   ├── mail_vifm.vim
│   │   │   ├── vifm-cmdedit.vim
│   │   │   ├── vifm-edit.vim
│   │   │   ├── vifm-rename.vim
│   │   │   └── vifm.vim
│   │   ├── plugin
│   │   │   └── vifm.vim
│   │   └── syntax
│   │       └── vifm.vim
│   └── vim-doc
│       └── doc
│           ├── tags
│           └── vifm-app.txt
└── zsh
    └── site-functions
        └── _vifm

```
