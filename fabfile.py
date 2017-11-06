from fabric.api import local, settings, abort, run, cd
from fabric.operations import get, sudo, put
from fabric.state import env
import os


env.user = 'hermes'
env.hosts = ['192.168.0.7']
env.conf_repo = 'https://github.com/megamorphf/env-configs.git'
env.parent_dir = '$HOME/diy'  # directory under which you store your confs and personal items
env.parent_rel = './diy'  # directory under which you store your confs and personal items
env.conf_folder = 'env-configs'
# looks like /home/hermes/diy/env-configs
env.conf_dir = os.path.join(env.parent_dir, env.conf_folder)
env.vundle_dir =  os.path.join(env.conf_dir, 'vim/hidden.vim/bundle')
env.branch = 'master'
env.alias = 'default'  # do not change this

def satellite():
    env.user = 'hermes'
    env.hosts = ['192.168.0.7']
    env.alias = 'satellite'
    env.install_manager = "apt install"


def hassio():
    env.user = 'root'
    env.hosts = ['192.168.0.105']
    env.alias = 'hassio'
    env.package_manager = ""


def pull_confs(first_time=False):

    if first_time:
        run('mkdir -p {}'.format(env.parent_dir))

    # create or pull all conf files
    with cd(env.parent_dir):
        if first_time:
            run("git clone {} --depth 1 --branch {} --single-branch {}".format(env.conf_repo, env.branch, env.conf_folder))
        else:
            run("git pull origin {}".format(env.branch))


def make_backup(filename, filedir='$HOME', ending='.bak'):
    """renames file to a backup file  script.sh --> script.sh.bak"""
    full_path = os.path.join(filedir, filename)
    run('(mv {file} {file}{ending}; exit 0)'.format(file=full_path, ending=ending))


def install_package(package_name):
    sudo("{install_manager} -y {package_name}".format(
        install_manager=env.install_manager,
        package_name=package_name))


def setup_tmux(confname='.tmux.conf', confdir='$HOME', conffile='tmux/hidden.tmux.conf'):
    make_backup(confname, confdir)

    with cd(confdir):
        targetdir = os.path.join(env.conf_dir, conffile)
        run('ln -s {} {}'.format(targetdir, confname))
        print("CREATING SYMLINK")
        run('ls -alt | grep {}'.format(confname))


def setup_vim():
    with cd('$HOME'):
        run("ln -s ./diy/env-configs/vim/vimrc-mac .vimrc")


def install_vundle():
    try:
        run("git clone https://github.com/VundleVim/Vundle.vim.git {}".format(env.vundle_dir))
    except Exception as e:
        print("Clonning failed vundle already probably installed: {}".format(e))

    finally:
        run("vim +PluginInstall +qall")


def get_bashrc():
    remote = '.bashrc'
    local = './bash/{}.bashrc'.format(env.alias)
    get(remote_path=remote, local_path=local)


def get_secrets():
    # remote = '/config/secrets.yaml'
    # local = './downloads/secrets.yaml'
    # get(remote_path=remote, local_path=local)

    secret_list = ['secrets.yaml', 'known_devices.yaml']

    for secret in secret_list:
        remote = os.path.join('/config', secret)
        localf = os.path.join('./downloads', secret)
        get(remote_path=remote, local_path=localf)


def setup_bash():
    pass


def first_full_install():
    pull_confs(True)
    install_package('vim')
    setup_vim()
    install_vundle()
    install_package('tmux')
    setup_tmux()

def test():
    pass

