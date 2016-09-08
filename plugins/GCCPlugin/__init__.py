from plugins.IPlugin import IBuildPlugin


class GCCPlugin(IBuildPlugin):

    def register(self):
        pass

    def getName(self):
        return "GCC"

    def build(self, variants):
        print "build"

    def clean(self):
        print "Clean"
