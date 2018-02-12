
echo "Doing music sync"
src='/media/root/kodi/music'
dst='/media/root/kodi-media/'
rsync -avog --progress --inplace --chown=nobody:nogroup --chmod=D755,F644 $src $dst


echo "Doing jazz sync"
src='/media/root/kodi/audiobooks/'
dst='/media/root/kodi-media/music/'
rsync -avog --progress --inplace --chown=nobody:nogroup --chmod=D755,F644 $src $dst

echo "Doing game full game sync"
src='/media/root/kodi/retro-pie-all/roms'
dst='/media/root/kodi-media/games/'
rsync -avog --progress --inplace --chown=nobody:nogroup --chmod=D755,F644 $src $dst


echo "Doing NES sync"
src='/media/root/kodi/RetroPie/roms/snes/'
dst='/media/root/kodi-media/games/roms/snes/'

rsync -avog --progress --inplace --chown=nobody:nogroup --chmod=D755,F644 $src $dst


echo "Doing movie sync"
src='/media/root/kodi/movies'
dst='/media/root/kodi-media/'
rsync -avog --progress --inplace --chown=nobody:nogroup --chmod=D755,F644 $src $dst


echo "Doing Series sync"
src='/media/root/kodi/series'
dst='/media/root/kodi-media/series/'
rsync -avog --progress --inplace --chown=nobody:nogroup --chmod=D755,F644 $src $dst
