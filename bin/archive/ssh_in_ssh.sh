#!/usr/bin/expect -f

# set the variables
set jumphost "84.38.45.23"
set ssh_user "bijan.rofoee"
set box "ar9.bllab"
#hide password input


send_user "enter password: "
#stty -echo
expect_user -re "(.*)\n"
#stty echo
set password $expect_out(1,string)
#puts "you said $password"




send_user "enter command: "
#stty -echo
expect_user -re "(.*)\n"
#stty echo
set command $expect_out(1,string)
#puts "you said $password"


puts "ssh -tt $ssh_user@$jumphost ssh -tt $ssh_user@$box $command"

spawn ssh -tt $ssh_user@$jumphost ssh -tt $ssh_user@$box $command

expect -- "*?assword:*"
send $password
interact
#before starting the next tunnel
sleep 1
expect -- "*?assword:*"
send $password
interact
#before starting the next tunnel
sleep 1

