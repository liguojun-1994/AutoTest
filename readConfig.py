import configparser
import os
import getpathInfo
import codecs

path=getpathInfo.get_Path()
configPath=os.path.join(path,'config.ini')
config=configparser.ConfigParser()
config.read(configPath,encoding='utf-8')


class ReadConfig:
    def get_database(self,name):
        values=config.get('Database',name)
        return values
    def get_Http(self,name):
        values=config.get('Http',name)
        return values
    def get_Email(self,name):
        values=config.get('Email',name)
        return values


if __name__ == '__main__':
    print(ReadConfig().get_database('host'))


