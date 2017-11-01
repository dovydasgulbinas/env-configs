from fabric.api import local, settings, abort, run, cd
from fabric.operations import get, sudo, put
from fabric.state import env
import os



env.user = 'hermes'
env.hosts = ['192.168.0.7']
env.conf_repo = 'https://github.com/megamorphf/env-configs.git'
env.parent_dir = '$HOME/diy'  # directory under which you store your confs and personal items
env.parent_rel = '.diy'  # directory under which you store your confs and personal items
env.conf_folder = 'env-configs'
# looks like /home/hermes/diy/env-configs
env.conf_dir = os.path.join(env.parent_dir, env.conf_folder)
env.branch = 'master'
env.alias = 'default'

def satellite():
    env.user = 'hermes'
    env.hosts = ['192.168.0.7']
    env.alias = 'satellite'


def pull_confs(first_time=True):

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


def setup_tmux(confname='.tmux.conf', confdir='$HOME', conffile='tmux/hidden.tmux.conf'):
    make_backup(confname, confdir)

    with cd(confdir):
        targetdir = os.path.join(env.conf_dir, conffile)
        run('ln -s {} {}'.format(targetdir, confname))
        print("CREATING SYMLINK")
        run('ls -alt | grep {}'.format(confname))


def get_bashrc():
    remote = '.bashrc'
    local = './bash/{}.bashrc'.format(env.alias)
    get(remote_path=remote, local_path=local)

def setup_bash():
    pass


def setup_all():
    setup_tmux()


def test():
    pass

