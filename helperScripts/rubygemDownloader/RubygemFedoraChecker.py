import requests
from RubygemKojiChecker import RubygemKojiChecker

class RubygemFedoraChecker(RubygemKojiChecker):

    def __init__(self):
        super(RubygemFedoraChecker,self).__init__("https://koji.fedoraproject.org/koji/search?match=glob&terms=")

