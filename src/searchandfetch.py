'''
Author          : Bijan R.Rofoee
Version         : 0.1
'''
import os


class Top:
    '''

    '''

    def __init__(self, topdir, filename):
        self.topdir = topdir
        self.filename = filename

    def return_name(self):
        return self.filename


class Searcher(Top):
    '''

    '''

    def __init__(self, topdir, filename):
        Top.__init__(self, topdir, filename)

    def search(self):
        '''

        :param topdir:
        :param filename:
        :return:
        '''
        for dirpath, dirnames, files in os.walk(self.topdir):
            for name in files:
                if self.filename in name.lower():
                    print(os.path.join(dirpath, name))
                    file_dir = (os.path.join(dirpath, name))
                    return file_dir


class Fetcher:
    '''

    '''

    def __init__(self, file_dir_):
        self.file_dir = file_dir_

    def fetcher(self):
        '''

        :return:
        '''
        print (self.file_dir)
        f = open(self.file_dir)
        k = f.readlines()
        conf = dict()
        cont = ''
        config_keyname = ''
        for j, i in enumerate(k):
            if 'node name' in i:
                # this is the trick
                conf[config_keyname] = cont

                # buffer the node name
                line_st = str(i)
                line_list = line_st.split('node name=')
                config_keyname = line_list[1].split()[0]

                # restart capturing config
                cont = ''
            cont = cont + str(i)
        return conf


def dic_pritner(conf_dic):
    '''

    :param conf_dic:
    :return:
    '''
    keys = conf_dic.keys()

    for i in keys:
        print (conf_dic[i])


def is_conf_available(conf_dic):
    '''

    :param conf_dic:
    :return:
    '''
    running_keys = list()
    keys = conf_dic.keys()
    for i in keys:
        if 'hostname' in str(conf_dic[i]):
            running_keys.append(i)

    return running_keys
    # for i in running_keys:
    #     print i


def clean_conf_block(conf_block):
    '''

    :return:
    '''
    clean_conf = list()
    for i in conf_block:
        if not (">" in i):
            clean_conf.append(i)
    # import pprint as pp
    # pp.pprint(clean_conf)
    conf_out = ('\n'.join(clean_conf))
    # print conf_out
    return conf_out


if __name__ == '__main__':
    #    topdir = '/Users/bra17/PycharmProjects/auto_unl/git_configs/INE-VIRL'
    labname = 'base.ipv4.virl'
    labname = 'l2vpn.virl'
    topdir = os.path.dirname(os.getcwd())

    T = Top(topdir, labname)
    S = Searcher(topdir, labname)
    file_dir = S.search()

    F = Fetcher(str(file_dir))
    conf_dic = F.fetcher()

    # dic_pritner(conf_dic)

    running_conf_keys = is_conf_available(conf_dic)

    print (running_conf_keys)
    # print conf_dic['"R1"']
    # print ".... happy cleaning"
    # clean_conf_block(conf_dic['"XR1"'].split('\n'))

    for i in running_conf_keys:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("config start for node :" , i )
        print(clean_conf_block(conf_dic[i].split('\n')))
        print("config end for node :" , i )


