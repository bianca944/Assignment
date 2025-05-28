#!/bin/bash
groupadd iotusers
useradd -m -G iotusers iotuser1
useradd -m -G iotusers iotuser2

mkdir -p /home/iotshared
chown :iotusers /home/iotshared
chmod 775 /home/iotshared
chmod g+s /home/iotshared
