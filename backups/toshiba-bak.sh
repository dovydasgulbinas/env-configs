
# 1. create a dir for mounting
# 2. mount `source` disk
# 3. create a dir in `destination` disk
# 4. recreacte folder structure in `destination` disk
# 5. groupdadd --gid=5000 media
# 5. chown -R root:media
# 6. chmod 771 -R 
# 7. chmod +s -R


srcbase='/media/root/kodi/var/backups/media-bak/kodi-media'
dstbase='/media/raid/media'

echo "Doing music sync"
src="$srcbase/music/"
dst="$dstbase/music"
rsync -avog --progress --inplace --chown=root:media --chmod=D775,F664 $src $dst


echo "Doing Misc Sync"
src="$srcbase/misc/"
dst="$dstbase/misc"  # you do not have to create destination dirs
rsync -avog --progress --inplace --chown=root:media --chmod=D775,F664 $src $dst


echo "Doing Movies Sync"
src="$srcbase/movies/"
dst="$dstbase/movies"
rsync -avog --progress --inplace --chown=root:media --chmod=D775,F664 $src $dst


echo "Doing Series Sync"
src="$srcbase/series/"
dst="$dstbase/series"
rsync -avog --progress --inplace --chown=root:media --chmod=D775,F664 $src $dst


echo "Doing Games Sync"
src="$srcbase/games/"
dst="$dstbase/games"
rsync -avog --progress --inplace --chown=root:media --chmod=D775,F664 $src $dst

