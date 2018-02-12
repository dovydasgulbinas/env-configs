

# install albert confs

main config

    confdir="~/.config/albert"
    ln -s ~/diy/env-configs/albert/albert.conf "$confdir/albert.conf"


extras
    
    repodir="$HOME/diy/env-configs"
    confdir="$HOME/.config/albert"
    mv "$confdir/org.albert.extension.websearch" "$confdir/org.albert.extension.websearch.bak"
    ln -s "$repodir/albert/org.albert.extension.websearch" "$confdir/org.albert.extension.websearch" 
