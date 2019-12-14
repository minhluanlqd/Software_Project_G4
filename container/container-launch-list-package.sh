#!/bin/bash

#container generation, listing and packaging
#name of the container garageloc3

echo "generating a container named garagaloc3"

lxc launch ubuntu:18.04 garagaloc3
sleep 8
lxc list

sleep 5
sudo tar -zcvf /root/garagaloc3.tar.gz /var/lib/lxd/storage-pools/default/containers/garagaloc3/
