# _*_ coding: UTF-8 _*_
import configparser as ConfigParser

class InitConfig(object):

    def __init__(self, path):
        self.path = path
        self.config = ConfigParser.ConfigParser()

    def getAllNodeItems(self,field):
        result = dict()
        try:
            self.config.read(self.path)
            keys = self.config.options(field)
        except ConfigParser.NoSectionError:
            return None
        for key in keys:
            result[key] = self.getValue(field,key)
        return result

    def getValue(self, field, key,type=None):
        result = None
        try:
            self.config.read(self.path)
            if(type == int):
                result = self.config.getint(field, key)
            else:
                result = self.config.get(field, key)
        except ConfigParser.NoSectionError:
            print("There is no the Section!")
        except ValueError:
            print("There is no value like int!")
        except:
            pass
        return result

    def setKeyValue(self, filed, key, value):
        try:
            self.config.read(self.path)
            self.config.options(filed)
        except ConfigParser.NoSectionError:
            self.config.add_section(filed)
        except:
            return False
        try:
            self.config.set(filed, key, value)
        except TypeError:
            self.config.set(filed, key, str(value))
        except:
            return False
        self.config.write(open(self.path,'w'))
        return True

if __name__ == "__main__":
    conf = InitConfig("ServerConfig.ini");
    print(conf.getValue("DataBase","host"));
    print(conf.getValue("DataBase","port"));
    print(conf.getValue("DataBase","user"));
    print(conf.getValue("DataBase","passwd"));
    print(conf.getValue("DataBase","db"));