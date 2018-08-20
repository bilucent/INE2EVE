'''
Author          : Bijan R.Rofoee
Email           : bijan.rofoee@sky.uk
Version         : 0.1
Date            : 01/03/2017
Subject         : segment routing and traffic steering app
'''
import datetime
import logging
import os
from time import time

from paramiko import SSHException
import napalm
from src.util import read_device_list, file_writer, file_finfer
from threading import Thread
device_list = "../bin/tunnel_auto/list_lab.txt"



from netmiko import ConnectHandler as CH, NetMikoTimeoutException
logging.basicConfig(filename="paramikologs.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")



class Scale_funcs():

    @staticmethod
    def backup_to_file(device_dict={}):

        threads = []

        if device_dict.values().__len__() is 0:
            _BN = Scale_funcs().Atomic_functions()
            _BN.fetch_config()
        else:
            _BN = Scale_funcs().Atomic_functions()
            # _BN.fetch_config()
            config = list()
            # for i in device_dict.values():
            #     t = (Thread(target=_BN.fetch_config,
            #                 kwargs={'dev_name': i[2], 'port': i[1], 'confg':config,
            #                         'device_type':"cisco_ios"}))
            #     t.start()
            #     t.join()
            #
            #     print(os.getpid(), t.name)
            #     threads.append(t)
            #     currentDT = datetime.datetime.now()
            #     file_name = "Node_"+ i[2] + "_"+ currentDT.strftime("%Y-%m-%d-%H")
            #     assert (config.__len__()>0)
            #     file_writer(file_name, config)

            for i in device_dict.values():
                # tt = _BN.fetch_config(dev_name=i[2], port=i[1], confg=config)
                _BN.fetch_config(dev_name=i[2], port=i[1], config=config, device_type="cisco_ios")
                currentDT = datetime.datetime.now()
                file_name = "Node_"+ i[2] + "_"+ currentDT.strftime("%Y-%m-%d-%H")
                assert (config.__len__()>0)
                file_writer(file_name, config)

    # TODO
    @staticmethod
    def command_all(device_dict={}):

        threads = []

        if device_dict.values().__len__() is 0:
            _BN = Scale_funcs().Atomic_functions()
            _BN.fetch_config()
        else:
            _BN = Scale_funcs().Atomic_functions()
            config = list()
            for i in device_dict.values():
                com = 'show run' \
                      'conf t' \
                      'ip scp server enable'

                _BN.send_command(dev_name=i[2], port=i[1], config=config, device_type="cisco_ios", command=com)
                currentDT = datetime.datetime.now()
                print(config)
                # file_name = "Node_"+ i[2] + "_"+ currentDT.strftime("%Y-%m-%d-%H")
                # assert (config.__len__()>0)
                # file_writer(file_name, config)

    @staticmethod
    def zero_reload_all(device_dict):
        zero_location ="../config/base_zero"
        files = file_finfer(zero_location)
        for i in files:
            config = open(i, 'r+').readlines()



    class Atomic_functions():
        @staticmethod
        def fetch_config(**kwargs):
            device = {
                "device_type":kwargs['device_type'],
                "ip":"127.0.0.1",
                "port":kwargs['port'],
                "username":"cisco",
                "password":"cisco"
                }
            try:
                netconnect = CH(**device)
                output = netconnect.send_command("show run")
                print("----config is for node---: ", kwargs['dev_name'])
                print("display output {}".format(output))
                # kwargs['config'] = output
                return kwargs['config'].append(output)
                # return output
            except (NetMikoTimeoutException, SSHException) as e:
                logging.error('===', e)

        @staticmethod
        def send_command(**kwargs):
            device = {
                "device_type":kwargs['device_type'],
                "ip":"127.0.0.1",
                "port":kwargs['port'],
                "username":"cisco",
                "password":"cisco"
                }
            try:
                netconnect = CH(**device)
                output = netconnect.send_command(kwargs['command'])
                print("----config is for node---: ", kwargs['dev_name'])
                return kwargs['config'].append(output)
            except (NetMikoTimeoutException, SSHException) as e:
                logging.error('===', e)

        @staticmethod
        def loadReplace_string(**kwargs):
            """Load a config for the device."""

            # Use the appropriate network driver to connect to the device:
            driver = napalm.get_network_driver(kwargs['device_type'])

            # Connect:
            device = driver(hostname=kwargs['host'], username='cisco',
                            password='cisco', optional_args={'port': kwargs['port']})

            print('Opening ...')
            device.open()

            print('Loading replacement candidate ...')
            device.load_replace_candidate(config=kwargs['config'])
            device.commit_config()

            device.close()
            print('Done.')


def simple_test(device_type="cisco_ios",
                     ip="127.0.0.1",
                     port="22205",
                     username="cisco",
                     password="cisco"):
        device = {
            "device_type": device_type,
            "ip": ip,
            "port": port,
            "username": username,
            "password": password
            }
        try:
            netconnect = CH(**device)
            output = netconnect.send_command("show run")
            print("display output {}".format(output))
        except NetMikoTimeoutException as err:
            logging.error('=== NetMikoTimeoutException')

if __name__=="__main__":
    device_dict = read_device_list()

    # Scale_funcs.backup_to_file(device_dict)
    # Scale_funcs.command_all(device_dict)
    Scale_funcs.zero_reload_all(device_dict)
    # Scale_funcs.loadReplace_string(device_dict)



    # simple_test()