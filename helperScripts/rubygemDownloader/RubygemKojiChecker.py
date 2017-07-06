import requests

class RubygemKojiChecker(object):

    def __init__(self,url):
        self.url = url 

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
        return self.check_package(package)
        #if not self.check_package(package):
        #   return self.check_rpm(package)
        #return self.isIn

    def parse (self):
        isIn = self.request.text.find ('<td colspan="2">No search results</td>')
        if (isIn == -1 ):
            textStart = self.request.text.find ('<h4>Information for ')
            textEnd = self.request.text.find('</a></h4>',textStart)
            self.packageUrl = self.request.text[textStart:textEnd]
            self.isIn = True

            # Need to find all the builds
            self.builds =[]
            startingCH =1
            while startingCH>0:
                build = {}
                #build ID
                buildTextStart = self.request.text.find ('buildinfo?buildID=',startingCH)
                if (buildTextStart<0):
                    break
                buildTextEnd = self.request.text.find ('"',buildTextStart)
                buildId = self.request.text[(buildTextStart+18):buildTextEnd]
                build['id'] = buildId 

                #package-name-version
                versionTextStart = self.request.text.find(">",buildTextEnd)
                versionTextEnd = self.request.text.find("<",versionTextStart)
                dashPosition = self.request.text.find("-",(versionTextStart+len(self.package)))

                #posible version 
                version = self.request.text[dashPosition:versionTextEnd]
                packageVersion = self.request.text[versionTextStart:versionTextEnd]
                build['version'] = version
                build['fullname'] = packageVersion 

                #status of the build
                statusTextStart = self.request.text.find ('<img class="stateimg"',versionTextEnd)
                statusTextStart = self.request.text.find ('title="',statusTextStart)
                statusTextEnd = self.request.text.find ('"',statusTextStart+7)
                status = self.request.text[(statusTextStart+7):statusTextEnd]
                build['status'] = status
                self.builds.append(build)
                startingCH = statusTextEnd

        else:
            self.isIn = False
            self.packageUrl = None

