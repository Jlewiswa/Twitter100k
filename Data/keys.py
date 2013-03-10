import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.cfg')

def getKey(section,setting):
    return config.get(section,setting)