'''
Author          : Bijan R.Rofoee
Email           : bijan.rofoee@sky.uk
Version         : 0.1
Date            : 01/03/2017
Subject         : segment routing and traffic steering app
'''

# crypto key generate rsa modulus 2048 label SSH

IOS_ssh = '''
!
!
#
conf t
username cisco password 0 cisco
no ip domain lookup
ip domain name cisco.com

ip ssh rsa keypair-name SSH
ip ssh version 2
!
'''

IOS_remote_logig = '''
!
!
conf t
line con 0
 exec-timeout 0 0
 logging synchronous
 transport preferred none
 stopbits 1
line vty 0 4
 exec-timeout 0 0
 login local
 transport input telnet ssh
line vty 5 15
 login local
!
!

'''

IOSXR_SSH = '''
!
conf t
!
xml agent tty
 iteration off
!
xml agent
 iteration off
!
ssh server v2
ssh server vrf default
ssh server netconf vrf default

'''
