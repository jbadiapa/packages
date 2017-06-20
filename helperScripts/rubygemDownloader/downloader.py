import RubygemDownloader
import RubygemParser
import RubygemCBSChecker 
import pprint 
import subprocess

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
            gemName = "{}.gem".format(gem)
            downloader.download_file(parser.link,gemName)
            process = subprocess.Popen(['gem2rpm',gemName], stdout=subprocess.PIPE)
            out, err = process.communicate()
            gemSpec = open ("{}.spec".format(gemName),"w")
            gemSpec.write(out)
            gemSpec.close()
            gems = gems + parser.devDeps + parser.runtimeDeps
        else:
            dependencies[gem]=cbsChecker.packageUrl
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
