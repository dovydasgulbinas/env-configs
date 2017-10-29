# env-configs

# This repo covers

- Albert
- Pycharm 2017
- zsh
- vimf
- bash
- git
- tmux

# Using the configuration

## 0. Choose any dir e.g: ~/diy/env-configs

```
mkdir $HOME/diy
```

## 1. clone this whole repo:

```
git clone git@github.com:megamorphf/env-configs.git $HOME/diy/env-configs
```

## 2. create symlinks to your conf files

```
# vim
cd $HOME && ln -s ./diy/env-configs/vim/basic.vimrc .vimrc

# vifm, OS X
cd $HOME/.config && ln -s ./diy/env-configs/vifm/ vifm

# vifm, Debian
cd $HOME && ln -s ./diy/env-configs/vifm/ vifm

# zsh
cd $HOME && ln -s ./diy/env-configs/zsh/.zshrc .zshrc

# git
cd $HOME && ln -s ./diy/env-configs/git/.gitignore_global .gitignore_global

```


## x. (optional) export $PATH variable for the scripts folder

```
# for bash
echo "export PATH=$HOME/diy/env-configs/scripts:$PATH" >> $HOME/.bashrc

# for zsh
echo "export PATH=$HOME/diy/env-configs/scripts:$PATH" >> $HOME/.bashrc
```




