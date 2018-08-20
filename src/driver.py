'''
Author          : Bijan R.Rofoee
Email           : bijan.rofoee@sky.uk
Version         : 0.1
Date            : 01/03/2017
Subject         : segment routing and traffic steering app
'''
import netmiko
import sys, os
sys.path.append(os.getcwd())
from netmiko import ConnectHandler
import etc.constants as const


class IOS:
    """
    this class contains IOS functions
    """
    def __init__(self):
        pass

    def connect_commit(self, hostname_ip, hostname_port, push_this):
        netmiko.__version__
        cisco_ios = {
            "device_type": "cisco_ios_ssh", "ip": hostname_ip,
            "username": "cisco", "password": "cisco", "port": hostname_port,
            }

        netcon = ConnectHandler(**cisco_ios)
        output = netcon.send_command('show ip int br')
        print (output)

        netcon.send_command_timing('ena')
        netcon.send_command_timing('cisco')
        netcon.send_command_timing('conf t')
        # netcon.send_command_timing('no ip routing')
        # netcon.send_command_timing('ip routing ')
        netcon.send_command_timing('default inter  gi 1 ')
        netcon.send_command_timing('default inter  gi 2 ')
        netcon.send_command_timing('default inter  gi 3 ')
        netcon.send_command_timing('default inter  gi 4 ')

        output = netcon.send_command_timing(push_this)
        len(output)
        print (output)

        netcon.disconnect()

    def test_connection(self):
        pass


class IOSXR:
    """
    this class contains IOSXR functions
    """
    def __init__(self):
        pass

    def connect_commit(self, hostname_ip, hostname_port, push_this):
        netmiko.__version__
        cisco_ios = {
            "device_type": "cisco_ios_ssh", "ip": hostname_ip,
            "username": "cisco", "password": "cisco", "port": hostname_port,
            }

        netcon = ConnectHandler(**cisco_ios)
        output = netcon.send_command('show ip int br')
        print (output)

        netcon.send_command_timing('ena')
        netcon.send_command_timing('cisco')
        netcon.send_command_timing('conf t')
        # netcon.send_command_timing('no ip routing')
        # netcon.send_command_timing('ip routing ')
        netcon.send_command_timing('default inter  gi 1 ')
        netcon.send_command_timing('default inter  gi 2 ')
        netcon.send_command_timing('default inter  gi 3 ')
        netcon.send_command_timing('default inter  gi 4 ')

        output = netcon.send_command_timing(push_this)
        len(output)
        print (output)

        netcon.disconnect()

    def test_connection(self):
        pass


if __name__ == "__main__":

    R1_config = '''
    !
        no service timestamp
        enable password cisco
        no ip domain lookup
        ip cef distributed
        !
        interface Loopback0
         ip address 1.1.1.1 255.255.255.255
        !
        interface GigabitEthernet2
         no shutdown
        !
        interface GigabitEthernet2.12
         encapsulation dot1Q 12
         ip address 10.1.2.1 255.255.255.0
         no shutdown
        !
        line con 0
         exec-timeout 0 0
         logging synchronous
         transport preferred none
        line vty 0 4
         login local
        !
        end
    '''
    ip = '127.0.0.1'
    port = 22221
    I = IOS()
    confg = R1_config + const.IOS_remote_logig + const.IOS_ssh
    I.connect_commit(ip, port, R1_config)
