#!/bin/bash
sudo fdisk -u /dev/sdb <<EOF
n
p
1


t
8e
w
EOF

pvcreate /dev/sdb1
vgextend linux /dev/sdb1
lvextend -l +100%FREE /dev/mapper/linux-root
xfs_growfs /dev/mapper/linux-root
mount -oremount,inode64 /dev/mapper/linux-root
