#!/bin/bash

##Set defaults##

if_net="eth0"
br_net="lxdbr0"
if_net_ip="10.160.41.98"
LXD clustering="no"
new storage pool="yes"
storage backend="btrfs"
size in gb="15GB"
local network bridge="yes"
lxd available over network="yes"
port to bind="8443"
stale cached images updated immidietly="yes"


$_snap install lxd

##Install branch of LXD##
$_apt install lxd lxd-client
$_apt install -t xenial-backports lxd lxd-client

##storage & network needs##
$_lxd init

##creating container##
$_lxc launch ubuntu:18.04 {container_name}
$_lxc list

##get a shell inside container##
$_lxc exec {container_name} -- /bin/bash
$_lxc exec {container_name} -- apt-get update

##application host##
$git clone "web URL"
$aplr Car1.jpg
$alpr Car2.jpg

##push files##
$_lxc file push hosts {container_name}/tmp/
$_lxc snapshot {container_name} {snapshot-name}

$_lxc stop {container_name}
$_lxc delete {container_name}

 
