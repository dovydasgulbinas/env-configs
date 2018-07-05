
# Check attached discs

    lsblk -io KNAME,TYPE,SIZE,MODEL


# Check disk health

    sudo smartctl -a /dev/sda >> hdd-health.log
    sudo smartctl -a /dev/sdb >> hdd-health.log
    sudo smartctl -a /dev/sdc >> hdd-health.log
    sudo smartctl -a /dev/sdd >> hdd-health.log


# Badblocks check

    sudo badblocks -v /dev/sda
    sudo badblocks -v /dev/sdb
    sudo badblocks -v /dev/sdc
    sudo badblocks -v /dev/sdd


# check speeds

    disk='/dev/sda';for i in 1 2 3; do sudo hdparm -tT $disk >> hdd-speeds.log; done; printf '=%.0s' {1..80} >> hdd-speeds.log
    disk='/dev/sdb';for i in 1 2 3; do sudo hdparm -tT $disk >> hdd-speeds.log; done; printf '=%.0s' {1..80} >> hdd-speeds.log
    disk='/dev/sdc';for i in 1 2 3; do sudo hdparm -tT $disk >> hdd-speeds.log; done; printf '=%.0s' {1..80} >> hdd-speeds.log
    disk='/dev/sdd';for i in 1 2 3; do sudo hdparm -tT $disk >> hdd-speeds.log; done; printf '=%.0s' {1..80} >> hdd-speeds.log
    

# disk mappings

  
    sda   disk 931.5G ST1000LM024 HN-M
    sdb   disk 931.5G ST1000LM014-SSHD (8GB Cache, Heating UP)
    sdc   disk 111.8G KINGSTON SV300S3
    sdd   disk 931.5G TOSHIBA MQ01ABD1


# RAID5 (from scratch)

    modprobe raid5  # enable raid kernel module
    cat /proc/mdstat  # check if modules was enabled
    mdadm --create /dev/md0 --verbose --force --assume-clean --level=5 --raid-devices=3 /dev/sda /dev/sdb /dev/sdd
    sudo mdadm --detail /dev/md0
    mkfs.ext4 /dev/md0  # build a ext4 files system on raid array
    blkid
    # uuid of new md0: UUID="94718039:cef3403b:bfa2a3a5:1fbc0682"
   

# Test Mount Device

    mount /dev/md/herver\:0 /media/raid/
    umount /dev/md/herver\:0


# Mount to fstab

    /dev/md/herver:0	/media/raid 	ext4 	auto,nofail,rw,user,async,dev,suid	0	2 
    mount -va


    
# touble shooting

- [Ooops my hdd had extra partitions thus not all HD was used][6]
- I need to wipe existing partitions

    wipefs -a /dev/sdX
    mkfs.ext4 /dev/sdX

- [I want to find speed gains using a raid][7]


# glossary

[spare disk][3]
:  a disk that is used temporarily when building raidX array. If you are
creating array on disks you dont mind loosing data with you dont need one



# resources

[1]: https://superuser.com/questions/171195/how-to-check-the-health-of-a-hard-drive
[2]: https://www.cyberciti.biz/tips/how-fast-is-linux-sata-hard-disk.html
[3]: https://serverfault.com/questions/43575/how-to-create-a-software-raid5-array-without-a-spare#43581
[4]: https://marc.info/?l=linux-raid&m=112044009718483&w=2
[5]: https://raid.wiki.kernel.org/index.php/RAID_setup#Options_for_mke2fs "archived: http://archive.is/P7sfg"
[6]: https://ubuntuforums.org/showthread.php?t=884556 "archived: http://archive.is/wMBWw"
[7]: http://www.raid-calculator.com/Default.aspx
