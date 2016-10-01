from plugins.IPlugin import IMiscPlugin


class CopyPlugin(IMiscPlugin):

    def register(self):
        self.addFnListener("run", self.run)

    def getName(self):
        return "COPY"

    def run(self, args):
        print "Run COPY"
