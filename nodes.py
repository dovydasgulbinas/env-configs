from fabric.decorators import task
from fabric.state import env


@task
def satellite():
    env.user = 'hermes'
    env.hosts = ['192.168.0.15']
    env.alias = 'satellite'
    env.install_manager = "apt install -y"


@task
def hassio():
    env.user = 'root'
    env.hosts = ['192.168.0.105']
    env.alias = 'hassio'
    env.install_manager = "apk add"
    env.secrets_dict = {
        "/config": ['secrets.yaml', 'known_devices.yaml', 'plex.conf'],
    }


@task
def kali():
    env.user = 'hermes'
    env.hosts = ['192.168.0.9']
    env.alias = 'kali'
    env.install_manager = "apt install -y"


@task
def mc():
    env.user = 'ud_dovydas_gulbinas'
    env.hosts = ['momentcredit.lt']
    env.alias = 'mc'
    env.install_manager = "yum install -y"


@task
def mcgit():
    env.user = 'ud_dovydas_gulbinas'
    env.hosts = ['194.0.160.3:1093']
    env.alias = 'mc'
    host_distro('debian')


@task
def plfab():
    env.user = 'fabric'
    env.hosts = ['pl-signature.local']
    env.alias = 'pl-signature'
    host_distro('debian')


@task
def herver():
    env.user = 'hermes'
    env.hosts = ['herver.local']
    env.alias = 'herver'
    host_distro('debian')



@task
def pl():
    env.user = 'fabric'
    env.hosts = ['mozipo.pl']
    env.internal_ip = '192.168.2.77'
    env.alias = 'pl'
    host_distro('centos')


def host_distro(os_name):
    if os_name == "debian":
        env.install_manager = "apt install -y"
    elif os_name == "centos":
        env.install_manager = "yum install -y"
    elif os_name == "resinon":
        env.install_manager = "apk add"
