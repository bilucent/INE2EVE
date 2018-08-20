'''
Author          : Bijan R.Rofoee
Email           : bijan.rofoee@sky.uk
Version         : 0.1
'''
import os

list_file_location = "../bin/tunnel_auto/list_lab.txt"


def read_device_list():
    file_list = []
    device_dict = dict()
    with open(os.getcwd()+"/"+list_file_location) as f:
        # print(f.readlines())
        file_list = f.readlines()
        file_dict = dict()
        for i in file_list:
            a, b, c = i.split()
            print(a)
            file_dict[a] = [b, c, a]

    return(file_dict)


def file_writer(name, content):
    '''

    :param name:
    :param content:
    :return:
    '''
    config_base_locaiton = "../config/base"
    with open(config_base_locaiton+"/"+name+".txt","w+") as f:
        f.write(''.join(content))
        f.close

def file_finfer(dir):
    file_list = list()
    for dirName, subdirList, fileList in os.walk(dir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            # print('\t%s' % fname)
            file_dir = (os.path.join(dirName, fname))
            file_full = os.path.abspath(file_dir)
            print(file_full)
            file_list.append(file_full)
    return file_list

# print(os.getcwd())
read_device_list()