'''
Author          : Bijan R.Rofoee
Email           : bijan.rofoee@sky.uk
Version         : 0.1
'''
from src.functions import Scale_funcs
from src.util import read_device_list


def pipe1_backup_nodes():
    device_dict = read_device_list()
    Scale_funcs.backuper(device_dict)


def pipe2_push_config():
    pass