#!/bin/bash


echo "sending the container over to another location"
scp root@node1-1:~/garagaloc3.tar.gz .
sleep 3

echo "unpacking container at the destination"
scp -r garagaloc3.tar.gz/ root@node1-2:/root/

sleep 2

ssh root@node1-2 "tar -zxvf /root/garagaloc3.tar.gz -C /"
