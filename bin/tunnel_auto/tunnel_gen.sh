#!/usr/bin/expect -f

# set the variables
set jumphost 10.246.65.138

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



set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22204:172.16.100.104:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22205:172.16.100.105:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22206:172.16.100.106:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22207:172.16.100.107:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22201:172.16.100.101:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22202:172.16.100.102:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22203:172.16.100.103:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22211:172.16.100.111:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22212:172.16.100.112:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22208:172.16.100.108:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22209:172.16.100.109:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1

set timeout -1
spawn ssh $ssh_user@$jumphost -fN -L 22210:172.16.100.110:22
expect -- "*?assword:*"
send "$password\n"
expect eof
sleep 1
