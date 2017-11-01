
# Installation of powerline
  
0. Install powerline executable
```
# anything with pip installed
pip install powerline-status
# OR
# debian
sudo apt-get install powerline

# test by running
powerline

```
1. Download and install the fonts for powerline
2. In your terminal choose one of the fonts containing name powerline
3. [Install powerline][poweline-install] bindings for other programs 

```
binddir="$HOME/diy/env-configs/powerline"

# basic install for zsh
powerline_zsh="$binddir/zsh/powerline.zsh"
if [[ -r $powerline_zsh ]]; then
    source $powerline_zsh
fi

```

[powerline-install]: "https://askubuntu.com/questions/283908/how-can-i-install-and-use-powerline-plugin#540730"
