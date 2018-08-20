'''
Author          : Bijan R.Rofoee
Email           : bijan.rofoee@sky.uk
Version         : 0.1
Date            : 01/03/2017
Subject         : segment routing and traffic steering app
'''
# import os
from src.searchandfetch import *
from src.driver import *

ip_dictionary = {
    '"R1"': '127.0.0.1',
    '"R2"': '127.0.0.1',
    '"R3"': '127.0.0.1',
    '"R4"': '127.0.0.1',
    '"R5"': '127.0.0.1',
    '"R6"': '127.0.0.1',
    '"R7"': '127.0.0.1',
    '"R8"': '127.0.0.1',
    '"R9"': '127.0.0.1',
    '"R10"': '127.0.0.1',
    '"XR1"': '127.0.0.1',
    '"XR2"': '127.0.0.1'
}

port_dictionary = {
    '"R1"': '22201',
    '"R2"': '22202',
    '"R3"': '22203',
    '"R4"': '22204',
    '"R5"': '22205',
    '"R6"': '22206',
    '"R7"': '22207',
    '"R8"': '22208',
    '"R9"': '22209',
    '"R10"': '22210',
    '"XR1"': '22221',
    '"XR2"': '22222'
}


#
# ip_dictionary = {'"R1"': '172.16.200.201',
#                  '"R2"': '172.16.200.202',
#                  '"R3"': '172.16.200.203',
#                  '"R4"': '172.16.200.204',
#                  '"R5"': '172.16.200.205',
#                  '"R6"': '172.16.200.206',
#                  '"R7"': '172.16.200.207',
#                  '"XR1"': '172.16.200.221',
#                  '"XR1"': '172.16.200.222'}

def start():
    """

    :return:
    """
    # labname = 'basic.eigrp.routing'
    labname = 'base.ipv4.virl'
    # topdir = os.path.dirname(os.getcwd())
    # topdir = os.path.dirname(__file__)
    topdir = os.getcwd()

    print topdir
    T = Top(topdir, labname)
    S = Searcher(topdir, labname)
    file_dir = S.search()

    F = Fetcher(str(file_dir))
    conf_dic = F.fetcher()

    # dic_pritner(conf_dic)

    running_conf_keys = is_conf_available(conf_dic)

    print running_conf_keys
    # print conf_dic['"R1"']
    # print ".... happy cleaning"
    # clean_conf_block(conf_dic['"XR1"'].split('\n'))

    for i in running_conf_keys:
        print i
        ip = ip_dictionary[i]
        config = clean_conf_block(conf_dic[i].split('\n'))
        print ip

        port = port_dictionary[i]

        # port = 22

        I = IOS()
        config = config + const.IOS_remote_logig + const.IOS_ssh
        I.connect_commit(ip, port, config)



if __name__ == '__main__':
    '''
    '''
    print 'bijan'
    topdir = os.getcwd()
    print topdir
    start()
