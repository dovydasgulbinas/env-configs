from fabric.context_managers import cd
from fabric.decorators import task, with_settings
from fabric.operations import run, sudo
from fabric.state import env


@task
def install_package(package_name):
    if env.user != 'root':  # some systems have `sudo` installed
        sudo("{install_manager} {package_name}".format(
            install_manager=env.install_manager,
            package_name=package_name))
    else:
        run("{install_manager} {package_name}".format(
            install_manager=env.install_manager,
            package_name=package_name))


@task
@with_settings(output_prefix=False)
def install_miniconda3(user=None, use_sudo=True, install_dir='~'):
    script_url = 'https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh'

    fname = 'miniconda3-installer.sh'
    install_package('bzip2')

    # if user and install_dir == '~':
    #     install_dir = install_dir + user
    #     print('using tilde expression for homedir: `{}`'.format(install_dir))

    with cd(install_dir):
        if user and use_sudo:
            sudo('wget --output-document {} {}'.format(fname, script_url),
                 user=user)
            sudo('chmod u+x {}'.format(fname), user=user)
            sudo('chown {0}:{0} {1}'.format(user, fname), user=user)
            sudo('/bin/bash {}'.format(fname), user=user)
            sudo("rm {}".format(fname), user=user)

        elif user and not use_sudo:
            run('wget --output-document {} {}'.format(fname, script_url))
            run('chmod u+x {}'.format(fname))
            run('chown {0}:{0} {1}'.format(user, fname))
            run("rm {}".format(fname))
            run('/bin/bash {}'.format(fname))
        else:
            run('wget --output-document {} {}'.format(fname, script_url))
            run('chmod u+x {}'.format(fname))
            run('chown $USER:$USER {}'.format(fname))
            run('/bin/bash {}'.format(fname))
            run("rm {}".format(fname))
