import time
import os

from fabric.api import local, settings, abort, run, cd
from fabric.operations import get, sudo, put
from fabric.state import env
from fabric.decorators import task, with_settings

import installers
from installers import install_package
import nodes

env.user = nodes._get_username()
env.hosts = ['127.0.0.1']
env.alias = 'localhost'  # do not change this

env.conf_repo = 'https://github.com/megamorphf/env-configs.git'
env.parent_dir = '$HOME/diy'  # directory under which you store your confs and personal items
env.parent_rel = './diy'  # directory under which you store your confs and personal items
env.conf_folder = 'env-configs'

# looks like /home/hermes/diy/env-configs
env.conf_dir = os.path.join(env.parent_dir, env.conf_folder)
env.vundle_dir = os.path.join(env.conf_dir, 'vim/hidden.vim/bundle')
env.vundle_package_dir = os.path.join(env.vundle_dir, 'Vundle.vim')
env.branch = 'master'


def dir_exists(directory, remote=True):
    cmd = '[ -d "{}" ]'.format(directory)
    with settings(warn_only=True):

        if remote:
            p = run(cmd)
        else:
            p = local(cmd)

        if p.return_code == 0:
            print("Directory `{}` exists".format(directory))
            return True
        else:
            print("Directory `{}` does not exist".format(directory))
            return False


def pull_confs():
    first_time = not dir_exists(env.conf_dir)
    # create or pull all conf files
    if first_time:
        run('mkdir -p {}'.format(env.parent_dir))
        with cd(env.parent_dir):
            run("git clone {} --depth 1 --branch {} {}".format(env.conf_repo,
                                                               env.branch,
                                                               env.conf_folder))
    else:
        with cd(env.conf_dir):
            run("git pull origin {}".format(env.branch))


def make_backup(filename, filedir='$HOME', ending='.bak'):
    """renames file to a backup file  script.sh --> script.sh.bak"""
    full_path = os.path.join(filedir, filename)

    run('(mv {file} {file}-{timestamp}-{ending}; exit 0)'.format(
        file=full_path, timestamp=get_timestamp(), ending=ending))


def get_timestamp():
    return int(time.time())


def setup_any(confname, confdir, conffile, conf_root_dir):
    """Takes a local config and install it on a host

    :param confname: file name that will be installed eg. .bashrc
    :param confdir: the directory in which we want to install eg. /home/jimmy
    :param conffile: relative path to the conf file on the host machine
    :return:
    """

    if not conf_root_dir:
        conf_root_dir = env.conf_dir

    make_backup(confname, confdir)
    with cd(confdir):
        targetdir = os.path.join(conf_root_dir, conffile)
        run('ln -s {} {}'.format(targetdir, confname))
        print("CREATING SYMLINK")
        run('ls -alt | grep {}'.format(confname))


def setup_tmux(conffile='tmux/hidden.tmux.conf', conf_root_dir=None):
    setup_any('.tmux.conf', '$HOME', conffile, conf_root_dir)


@task
def setup_newsboat(conffile='app-shares/main.newsboat', conf_root_dir='$SYNC_DIR'):
    """newsboat requires a cache folder in my case"""
    setup_any('.newsboat', '$HOME', conffile, conf_root_dir)


def setup_vim(vimrc='vim/vimrc-mac', vim='vim/hidden.vim', conf_root_dir=None):
    setup_any('.vimrc', '$HOME', vimrc, conf_root_dir)
    setup_any('.vim', '$HOME', vim, conf_root_dir)


def setup_git(gitconfig='git/.gitconfig',
              gitignore_global='git/.gitignore_global'):
    """
    cd $HOME && ln -s ./diy/env-configs/git/.gitignore_global .gitignore_global
    cd $HOME && ln -s ./diy/env-configs/git/.gitconfig .gitconfig
    """
    setup_any(".gitignore_global", '$HOME', 'git/.gitconfig')
    setup_any(".gitignore_global", '$HOME', 'git/.gitignore_global')


def setup_bash(profile_conf,alias_conf, func_conf, bashrc_conf, conf_root_dir=None):
    raise NotImplementedError("Write the magic function first!")
    pass


def install_vundle():
    try:
        run('mkdir -p {}'.format(env.vundle_dir))
        run("git clone https://github.com/VundleVim/Vundle.vim.git {}".format(
            env.vundle_package_dir))
    except Exception as e:
        print(
            "Clonning failed vundle already probably installed: {}".format(e))

    finally:
        run("vim +PluginInstall +qall")


def get_bashrc():
    remote = '.bashrc'
    local = './bash/{}.bashrc'.format(env.alias)
    get(remote_path=remote, local_path=local)


def get_pubkey():
    remote = "~/.ssh/id_rsa.pub"
    local = './downloads/{}.id_rsa.pub'.format(env.alias)
    get(remote_path=remote, local_path=local)



def get_privkey():
    remote = "~/.ssh/id_rsa"
    local = './downloads/{}.id_rsa'.format(env.alias)
    get(remote_path=remote, local_path=local)



def get_secrets(use_alias=False):
    for sdir in env.secrets_dict.iterkeys():
        fnames = env.secrets_dict[sdir]
        for fname in fnames:
            remote = os.path.join(sdir, fname)
            if use_alias:
                localf = os.path.join('./downloads',
                                      "-{}-{}".format(env.alias, fname))
            else:
                localf = os.path.join('./downloads', fname)
            get(remote_path=remote, local_path=localf)


@task
def install_pub_key():
    pub_key = local('cat $HOME/.ssh/id_rsa.pub', capture=True)

    if dir_exists("$HOME/.ssh"):
        with cd("$HOME/.ssh"):
            run('echo "{}" >> authorized_keys'.format(pub_key))
    else:
        run('ssh-keygen -t rsa -f "$HOME/.ssh/id_rsa" -q -P ""')
        run('echo "{}" >> $HOME/.ssh/authorized_keys'.format(pub_key))
        run('chmod 700 $HOME/.ssh')
        run('chmod 600 $HOME/.ssh/authorized_keys')
        run('chmod 400 $HOME/.ssh/id_rsa.pub')
        run('chmod 400 $HOME/.ssh/id_rsa')


def grant_sudo(username):
    cmd = 'usermod -aG sudo {}'.format(username)

    if username == env.user:
        print("You cant give `sudo` rights for the same user")
        return False

    if env.user == 'root':
        run(cmd)
    else:
        sudo(cmd)

    return True


def setup_hassio(conf_root_dir=None):
    first_full_install()
    setup_any('.profile', '$HOME', 'ash/hidden.profile', conf_root_dir)


@task
@with_settings(output_prefix=False)
def first_full_install():

    if env.local:
        pass
    else:
        install_pub_key()

    install_package('git')
    setup_git()
    pull_confs()
    install_package('vim')
    setup_vim()
    install_vundle()
    install_package('tmux')
    setup_tmux()


def test():
    pass
