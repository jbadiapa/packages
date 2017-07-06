from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class RubygemParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.isRuntime = False
        self.runtimeDeps = []
        self.isDev = False
        self.devDeps = []
        self.isGem = False
        self.link = None
        self.ruby_version = None
        self.isRubyVersion = False
        self.version = None
        self.isVersion = False

    def handle_starttag(self, tag, attrs):
        if (tag == 'div'):
            for attr in attrs:
                if (attr[0] == 'id' and  attr[1] == 'runtime_dependencies'):
                   self.isRuntime = True
                if (attr[0]=='id' and attr[1] == 'development_dependencies'):
                   self.isDev = True
        if (tag == 'strong'):
            self.isGem = True
        if (tag == 'a'):
            aux = {}
            for attr in attrs:
                if attr[0] == 'id':
                    aux['id']=attr[1]
                elif attr[0] == 'href':
                    aux['href']=attr[1]
            if aux.has_key('id') and aux['id'] == 'download':
                if aux.has_key('href'):
                    self.link = aux['href']
        if (tag == 'i'):
            for attr in attrs:
                if attr[0] == 'class':
                    if (attr[1] == 'gem__ruby-version'):
                        self.isRubyVersion = True;
                    elif (attr[1] == 'page__subheading'):
                        self.isVersion = True

    def handle_endtag(self, tag):
        if (self.isRuntime and tag == 'div'):
            self.isRuntime = False
        elif (self.isDev and tag == 'div'):
            self.isDev = False
        elif self.isGem and tag == 'strong':
            self.isGem = False
        elif self.isRubyVersion and tag == 'i':
            self.isRubyVersion = False
        elif self.isVersion and tag == 'i':
            self.isVersion = False

    def handle_data(self, data):
        if (self.isGem):
            if (self.isRuntime):
                self.runtimeDeps.append(data)
            elif (self.isDev):
                self.devDeps.append(data)
        elif self.isRubyVersion:
            pos = data.find("\n")
            if (pos > 0):
                self.ruby_version = data[:pos]
            else:
                self.ruby_version = data
        elif self.isVersion:
            self.version = data





