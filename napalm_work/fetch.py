# Sample script to demonstrate loading a config for a device.
#
# Note: this script is as simple as possible: it assumes that you have
# followed the lab setup in the quickstart tutorial, and so hardcodes
# the device IP and password.  You should also have the
# 'new_good.conf' configuration saved to disk.
from __future__ import print_function
import json
import napalm
import sys
import os

import datetime

from napalm.base.exceptions import ConnectionException


def get_hosts():
    with open("hosts.json", "r+") as f:
        hosts = json.load(f)
        f.close()
    return hosts


def archive(hostname = "127.0.0.1", port = "22"):
    config_file = ""
    # if not (os.path.exists(config_file) and os.path.isfile(config_file)):
    #     msg = 'Missing or invalid config file {0}'.format(config_file)
    #     raise ValueError(msg)
    print()
    # print('Loading config file {0}.'.format(config_file))

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver('ios')

    # Connect:


    device = driver(hostname=hostname, username='cisco',
                    password='cisco', optional_args={'port': port})

    print('Opening ...')
    device.open()

    print('get config  ...')
    conf = device.get_config()
    timenow = datetime.datetime.now()
    timeformatted = str(timenow.year) + "-" + str(timenow.month) + "-" + str(timenow.day) + "-" \
                    + str(timenow.hour) + "-" + str(timenow.minute) + "-"

    with open("_"+hostname+"_"+port + "_" + timeformatted +  ".json", "w+") as f:
        f.write(str(conf))
    f.close()

def main(config_file):
    """Load a config for the device."""
    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = 'Missing or invalid config file {0}'.format(config_file)
        raise ValueError(msg)
    print()
    # print('Loading config file {0}.'.format(config_file))

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver('ios')

    # Connect:
    device = driver(hostname='127.0.0.1', username='cisco',
                    password='cisco', optional_args={'port': 9000})

    print('Opening ...')
    device.open()

    print('Loading replacement candidate ...')
    device.load_replace_candidate(filename=config_file)
    device.get_config()

    # Note that the changes have not been applied yet. Before applying
    # the configuration you can check the changes:
    print('\nDiff:')
    print(device.compare_config())

    # You can commit or discard the candidate changes.
    try:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        device.commit_config()
    else:
        print('Discarding ...')
        device.discard_config()

    # close the session with the device.
    device.close()
    print('Done.')

    def compare():
        if len(sys.argv) < 2:
            print('Please supply the full path to "new_good.conf"')
            sys.exit(1)
        config_file = sys.argv[1]
        main(config_file)
if __name__ == '__main__':
    gh = get_hosts()
    for i in list(gh.keys()):
        print(i, gh[i])
        try:
            archive(gh[i], "22")
        except ConnectionException as err:
            print(err)
    # config()
    # comapre()
    # if len(sys.argv) < 2:
    #     print('Please supply the full path to "new_good.conf"')
    #     sys.exit(1)
    # config_file = sys.argv[1]
    # main(config_file)