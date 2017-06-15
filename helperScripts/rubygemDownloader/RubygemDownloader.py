import requests

class RubygemDownloader(object):

    def __init__(self):
        self.url = "https://rubygems.org/gems/"

    def download (self,gem):
        self.gem = gem
        self.request = requests.get ("{}{}".format(self.url,self.gem))

