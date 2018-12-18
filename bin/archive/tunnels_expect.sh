#!/usr/bin/expect -f

# set the variables
set jumphost "84.38.45.23"
#set ssh_user "bijan.rofoee"

#hide password input


send_user "enter username: "
#stty -echo
expect_user -re "(.*)\n"
#stty echo
set ssh_user $expect_out(1,string)
#puts "you said $password"



send_user "enter password: "
#stty -echo
expect_user -re "(.*)\n"
#stty echo
set password $expect_out(1,string)
#puts "you said $password"



set lab_router_ip_0 "89.200.128.225"
set lab_router_port_map_0 "30000"

set lab_router_ip_1 "89.200.128.245"
set lab_router_port_map_1 "30001"

set lab_router_ip_2 "84.38.34.250"
set lab_router_port_map_2 "30002"



set timeout -1
puts "ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_0:$lab_router_ip_0:22"
spawn ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_0:$lab_router_ip_0:22
expect -- "*?assword:*"
send $password
interact
##before starting the next tunnel
sleep 1

set timeout -1
puts "ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_1:$lab_router_ip_1:22"
spawn ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_1:$lab_router_ip_1:22
expect -- "*?assword:*"
send $password
interact
##before starting the next tunnel
sleep 1


set timeout -1
puts "ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_2:$lab_router_ip_2:22"
spawn ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_2:$lab_router_ip_2:22
expect -- "*?assword:*"
send $password
interact
##before starting the next tunnel
sleep 1





# test the tunnels
#netstat -na -p tcp -v -x


#
#
#An especially good solution for scripting is to use "master" mode, with a socket for control commands:
#
#ssh -f -N -M -S <path-to-socket> -L <post>:<host>:<port> <server>
#To close it again:
#
#ssh -S <path-to-socket> -O exit <server>
#This avoids both grepping for process ids and any timing issues that might be associated with other approaches.
