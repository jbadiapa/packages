import requests

class RubygemCBSChecker(object):

    def __init__(self):
        self.url = "http://cbs.centos.org/koji/search?match=glob&terms="

    def check_package(self,package):
        return self.check_url(package,"package")

    def check_rpm(self,package):
        return self.check_url("{}*".format(package),"rpm")

    def check_url(self,criteria,search):
        self.request = requests.get ("{}{}&type={}".format(self.url,criteria,search))
        self.parse()
        return self.isIn

    def check (self,package):
        self.package = package
        if not self.check_package(package):
           return self.check_rpm(package)
        return self.isIn

    def parse (self):
        isIn = self.request.text.find ('<td colspan="2">No search results</td>')
        if (isIn == -1 ):
            textStart = self.request.text.find ('<h4>Information for ')
            textEnd = self.request.text.find('</a></h4>',textStart)
            self.packageUrl = self.request.text[textStart:textEnd]
            self.isIn = True
        else:
            self.isIn = False
            self.packageUrl = None

