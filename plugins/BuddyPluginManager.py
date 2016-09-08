import os
import imp
from plugins.EventHook import EventHook


class BuddyPluginManager:

    pluginFolder = "./plugins"
    mainModule = "__init__"
    pluginFn = {}

    def __init__(self):
        self.onChange = EventHook()  # Not implemented yet TODO fires when code changes
        self.onScriptChange = EventHook()
        self.onDependencyChange = EventHook()
        plugins = self.getPlugins()
        for i in plugins:
            print "Loading plugin {}".format(i["name"])
            module = self.loadPlugin(i)
            pluginClass = getattr(module, i["name"])
            pluginClass(self)
            print "{} loaded successfully".format(i["name"])

    def getPlugins(self):
        plugins = []
        possibleplugins = os.listdir(self.pluginFolder)
        for i in possibleplugins:
            if i.__contains__("Plugin"):
                location = os.path.join(self.pluginFolder, i)
                if not os.path.isdir(location) or not self.mainModule + ".py" in os.listdir(location):
                    continue
                info = imp.find_module(self.mainModule, [location])
                plugins.append({"name": i, "info": info})
        return plugins

    def loadPlugin(self, plugin):
        return imp.load_module(self.mainModule, *plugin["info"])

    def addListener(self, plugin, name, fn):
        self.pluginFn.update({plugin: {name: fn}})
        print "Added method '{}' from plugin '{}'".format(name, plugin)

    def removeListener(self, plugin, name):
        self.pluginFn.__getitem__(plugin).__delitem__(name)
        print "Removed method '{}' from plugin '{}'".format(name, plugin)

    def getListener(self, plugin, name):
        return self.pluginFn[plugin][name]


BuddyPluginManager()