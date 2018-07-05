#sudo blkid
#mkfs.ext4 /dev/sdc5
#e2label /dev/sdc5 kodi-media
#[1]: https://serverfault.com/questions/796330/how-do-i-set-destination-permissions-with-rsync-chown-chmod#796341


echo "Doing backup sync"
src='/media/hermes/kodi-media'
dst='/media/hermes/0201547f-977c-4b4c-9982-823a89113a0a/var/backups/media-bak'
rsync -avog --progress --inplace --chown=nobody:nogroup --chmod=D755,F644 $src $dst


