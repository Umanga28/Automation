import configparser
import os

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

def configRead(section, key):
    config = configparser.ConfigParser()
    config_path = os.path.join(BASE_DIR, "ConfigurationFiles", "Config.cfg")
    config.read(config_path)
    return config.get(section, key)

def ElementsRead(section, key):
    config = configparser.ConfigParser()
    elements_path = os.path.join(BASE_DIR, "ConfigurationFiles", "Elements.cfg")
    config.read(elements_path)
    return config.get(section, key)


#print(configRead('Details','APP_URL'))