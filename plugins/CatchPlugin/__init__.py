from plugins.IPlugin import ITestPlugin


class CatchPlugin(ITestPlugin):

    def register(self):
        pass

    def test(self, args):
        pass

    def getName(self):
        return "BUDDY"
