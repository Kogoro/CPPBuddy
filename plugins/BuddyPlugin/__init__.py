from plugins.IPlugin import IMiscPlugin


class BuddyPlugin(IMiscPlugin):

    def run(self, args):
        print "ERROR: RUN NOT USED. PLEASE USE CLEAN INSTEAD!"
        pass

    def register(self):
        self.addFnListener("clean", self.clean)

    def getName(self):
        return "BUDDY"

    def clean(self, args):
        print "Clean {} {}".format(self.name, args)
