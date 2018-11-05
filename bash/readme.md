
1. symlink the main `.bash_profiles`
    cd env-configs/bash
    ln -s "$(pwd)/main.bash_profile" $HOME/.bash_profile
    source $HOME/.bash_profile

2. symlink `.bashrc`

    ln -s "$ENV_CONFIG_DIR/bash/main.bashrc" $HOME/.bashrc
    
3. symlink `.bash_aliases`

    ln -s "$ENV_CONFIG_DIR/bash/main.bash_aliases" "$HOME/.bash_aliases"

4. symlink `.bash_funcs`

    ln -s "$ENV_CONFIG_DIR/bash/main.bash_funcs" "$HOME/.bash_funcs"

5. symlink `.bash_modules` and add to $PATH

    ln -s "$ENV_CONFIG_DIR/bash/main.bash_modules" "$HOME/.bash_modules"

    
