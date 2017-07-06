import requests
from RubygemKojiChecker import RubygemKojiChecker

class RubygemCBSChecker(RubygemKojiChecker):

    def __init__(self):
        super(RubygemCBSChecker, self).__init__("http://cbs.centos.org/koji/search?match=glob&terms=")

