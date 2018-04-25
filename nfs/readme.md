
# [How NFS mount][1]


### Install client deps

    sudo apt-get update
    sudo apt-get install nfs-common


### Create Dirs on client

    sudo mkdir -p /mnt/nfs4/media/movies
    sudo mkdir -p /mnt/nfs4/media/music
    sudo mkdir -p /mnt/nfs4/media/series
    sudo mkdir -p /mnt/nfs4/media/games
    sudo mkdir -p /mnt/nfs4/media/downloads


### If you want to mount it manually

    sudo mount 192.168.0.8:/srv/nfs4/movies /mnt/nfs4/media/movies
    sudo mount 192.168.0.8:/srv/nfs4/series /mnt/nfs4/media/music
    sudo mount 192.168.0.8:/srv/nfs4/series /mnt/nfs4/media/series
    sudo mount 192.168.0.8:/srv/nfs4/games /mnt/nfs4/media/games
    sudo mount 192.168.0.8:/srv/nfs4/downloads /mnt/nfs4/media/downloads


### Client `/etc/fstab` entries

    192.168.0.8:/srv/nfs4/music /mnt/nfs4/media/music nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0
    192.168.0.8:/srv/nfs4/movies /mnt/nfs4/media/movies nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0
    192.168.0.8:/srv/nfs4/series /mnt/nfs4/media/series nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0
    192.168.0.8:/srv/nfs4/games /mnt/nfs4/media/games nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0
    192.168.0.8:/srv/nfs4/downloads /mnt/nfs4/media/downloads nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0


### Test If Shares

    df -h
    mount -t nfs



[1]: https://www.howtoforge.com/how-to-configure-a-nfs-server-and-mount-nfs-shares-on-ubuntu-14.04
[1a]: https://archive.fo/pnmwj
