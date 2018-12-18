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


# pr2.bllab
set lab_router_ip_0 "89.200.128.225"
set lab_router_port_map_0 "30000"

# ar9.bllab
set lab_router_ip_1 "89.200.128.245"
set lab_router_port_map_1 "30001"

# sr15
set lab_router_ip_2 "84.38.34.250"
set lab_router_port_map_2 "30002"

# pr2.hobir
set lab_router_ip_3 "89.200.128.102"
set lab_router_port_map_3 "30003"

# sr10.endnd
set lab_router_ip_4 "84.38.34.191"
set lab_router_port_map_4 "30004"




set timeout -1
puts "ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_0:$lab_router_ip_0:22"
spawn ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_0:$lab_router_ip_0:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
puts "ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_1:$lab_router_ip_1:22"
spawn ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_1:$lab_router_ip_1:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1


set timeout -1
puts "ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_2:$lab_router_ip_2:22"
spawn ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_2:$lab_router_ip_2:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1


set timeout -1
puts "ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_3:$lab_router_ip_3:22"
spawn ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_3:$lab_router_ip_3:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
puts "ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_4:$lab_router_ip_4:22"
spawn ssh $ssh_user@$jumphost -fN -L $lab_router_port_map_4:$lab_router_ip_4:22
expect -- "*?assword:*"
send "$password\n"
expect eof

