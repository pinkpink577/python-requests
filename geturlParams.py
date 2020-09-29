# @describe:将参数动态化

import readConfig

readconfig = readConfig.ReadConfig()


class GeturlParams(object):
    def get_Url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':8888' + '/query1' + '?'
        return new_url


if __name__ == '__main__':
    print(GeturlParams().get_Url())
