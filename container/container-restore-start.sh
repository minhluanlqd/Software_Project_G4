#!/bin/bash

lxc list
sleep 6

ln -s /var/lib/lxd/storage-pools/default/containers/garagaloc3/

echo "importing the final memory to the destination"

lxd import garagaloc3

echo "list of the newly added container to the destination location"

lxc list

sleep 6

echo "starting the new migrated container"

lxc start garagaloc3

lxc list

sleep 6
echo "start executing the container"

lxc exec garagaloc3 -- /bin/bash
sleep 4

#container delete
exit
lxc stop garageloc3
lxc delete garageloc3
