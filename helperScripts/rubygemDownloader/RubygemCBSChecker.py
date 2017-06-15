import requests

class RubygemCBSChecker(object):

    def __init__(self):
        self.url = "http://cbs.centos.org/koji/search?match=glob&type=package&terms="

    def check (self,package):
        self.package = package
        self.request = requests.get ("{}{}".format(self.url,self.package))
        self.parse()
        return self.isIn

    def parse (self):
        isIn = self.request.text.find ('<td colspan="2">No search results</td>')
        if (isIn == -1 ):
            textStart = self.request.text.find ('<h4>Information for package <a href="')
            textEnd = self.request.text.find('{}</a></h4>'.format(self.package),textStart)
            self.packageUrl = self.request.text[textStart:textEnd]
            self.isIn = True
        else:
            self.isIn = False
            self.packageUrl = None

