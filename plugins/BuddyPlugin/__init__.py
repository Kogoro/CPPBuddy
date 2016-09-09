from plugins.IPlugin import IMiscPlugin


class BuddyPlugin(IMiscPlugin):

    def register(self):
        self.addFnListener("clean", self.clean)

    def getName(self):
        return "BUDDY"

    def clean(self):
        print "Clean {}".format(self.name)
