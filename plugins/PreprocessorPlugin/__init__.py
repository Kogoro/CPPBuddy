from plugins.IPlugin import IMiscPlugin


class PreprocessorPlugin(IMiscPlugin):

    def register(self):
        self.addFnListener("run", self.run)

    def getName(self):
        return "PREPROCESSOR"

    def run(self):
        print "Run Preprocessor"
