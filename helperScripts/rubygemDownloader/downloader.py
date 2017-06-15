import RubygemDownloader
import RubygemParser
import RubygemCBSChecker 

gems =  ['webmock']

gem = gems.pop(0)

runtimeDeps = []
devDeps = []
dependencies ={}
doneGems = []

while gem:
    if (doneGems.count(gem) == 0):
        cbsChecker = RubygemCBSChecker.RubygemCBSChecker()
        if ((not cbsChecker.check('rubygem-{}'.format(gem))) and
            (not (cbsChecker.check(gem)))):
            downloader = RubygemDownloader.RubygemDownloader()
            parser = RubygemParser.RubygemParser()
            downloader.download(gem)
            parser.feed(downloader.request.text)
            runtimeDeps = runtimeDeps + parser.runtimeDeps
            devDeps = devDeps + parser.devDeps
            dependencies[gem]={'run':parser.runtimeDeps, 'dev':parser.devDeps, 'download':parser.link}
            gems = gems + parser.runtimeDeps + parser.devDeps
        else:
            dependencies[gem]=cbsChecker.packageUrl[37:-2]

    if len(gems)>0:
        gem = gems.pop(0)
    else:
        gem = None

print runtimeDeps
print 
print devDeps
print 
print doneGems
print
print dependencies

