from plugins.IPlugin import IBuildPlugin
import plugins.PluginHelperFunctions as helper
from subprocess import Popen
from os import environ, pathsep


class GCCPlugin(IBuildPlugin):
    def register(self):
        pass

    def getName(self):
        return "GCC"

    def build(self, args):
        print self.curVariant.parameters

        print helper.isTrue(self.curVariant.parameter('isLib').values[0])
        try:
            self.printer.info(environ['GCC_EXEC_PREFIX'].split(pathsep))
            # get all source files from the src dir
            # isLIb
            # include Headers
            # p = Popen(environ['GCC_EXEC_PREFIX'], '-Wall', )
            # p.communicate()
        except KeyError:
            self.printer.error("NOT FOUND GCC")

        print "build"

    def clean(self, args):
        print "Clean"
