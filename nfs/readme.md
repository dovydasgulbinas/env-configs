
# [How NFS mount][1]


### If you want to mount it manually

    sudo mount 192.168.0.8:/srv/nfs4/movies /mnt/nfs4/media/movies
    sudo mount 192.168.0.8:/srv/nfs4/series /mnt/nfs4/media/series
    sudo mount 192.168.0.8:/srv/nfs4/games /mnt/nfs4/media/games
    sudo mount 192.168.0.8:/srv/nfs4/downloads /mnt/nfs4/media/downloads


### /etc/fstab entries

    192.168.0.8:/srv/nfs4/music /mnt/nfs4/media/music nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0
    192.168.0.8:/srv/nfs4/movies /mnt/nfs4/media/movies nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0
    192.168.0.8:/srv/nfs4/series /mnt/nfs4/media/series nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0
    192.168.0.8:/srv/nfs4/games /mnt/nfs4/media/games nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0
    192.168.0.8:/srv/nfs4/downloads /mnt/nfs4/media/downloads nfs auto,noatime,nolock,bg,nfsvers=4,intr,tcp,actimeo=1800 0 0




[1]: https://www.howtoforge.com/how-to-configure-a-nfs-server-and-mount-nfs-shares-on-ubuntu-14.04
[1a]: https://archive.fo/pnmwj
