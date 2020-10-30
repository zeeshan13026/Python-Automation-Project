import configparser
import os


class ReadConfiguration():

    conf = None
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(os.getcwd()+"/MainResource/Conf/configuration.ini")

    def getApplicationUrl(self):
        return self.conf["BROWSER"]["url"]

    def getImplicitWait(self):
        return self.conf["BROWSER"]["implicitWait"]

    def getMaximizeBrowser(self):
        return self.conf["BROWSER"]["MaximizeBrowser"]



