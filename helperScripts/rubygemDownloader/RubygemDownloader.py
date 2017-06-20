import requests

class RubygemDownloader(object):

    def __init__(self):
        self.url = "https://rubygems.org/"

    def download (self,gem):
        self.gem = gem
        self.request = requests.get ("{}/gems/{}".format(self.url,self.gem))
 
    # This function from 
    # https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    def download_file(self,url,filename):
        self.filename = filename
        # NOTE the stream=True parameter
        r = requests.get("{}{}".format(self.url,url), stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
        return filename
