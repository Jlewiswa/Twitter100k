import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.cfg')

# Grab data from the config file based on section and setting
def getKey(section,setting):
    return config.get(section,setting)