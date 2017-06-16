import RubygemDownloader
import RubygemParser
import RubygemCBSChecker 
import pprint 

gems =  ['fluent-plugin-kubernetes_metadata_filter']

gem = gems.pop(0)

runtimeDeps = []
devDeps = []
dependencies ={}
doneGems = []

while gem:
    print (gem)
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
            gems = gems + parser.devDeps
        else:
            dependencies[gem]=cbsChecker.packageUrl[37:-2]
        doneGems.append(gem)

    if len(gems)>0:
        gem = gems.pop(0)
    else:
        gem = None
    with open ('fluent-plugin-kubernetes_metadata_filter','w') as out:
        pp = pprint.PrettyPrinter(indent=1,stream=out)
        pp.pprint(dependencies)

pp = pprint.PrettyPrinter(indent=1)
pp.pprint(dependencies)
