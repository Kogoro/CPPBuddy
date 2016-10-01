import os
import imp

from BuddyScript import BuddyPrinter
from plugins.EventHook import EventHook


class BuddyPluginManager:

    pluginFolder = "./plugins"
    mainModule = "__init__"
    pluginFn = {}

    def __init__(self, debug):
        """

        @param debug: True -> Show debug msgs
        @since 0.0.1-beta
        """
        self.printer = BuddyPrinter(debug)
        self.onChange = EventHook()  # Not implemented yet TODO fires when code changes
        self.onScriptChange = EventHook()
        self.onDependencyChange = EventHook()
        plugins = self.getPlugins
        for i in plugins:
            self.printer.debug("Loading plugin {}".format(i["name"]))
            module = self.loadPlugin(i)
            pluginClass = getattr(module, i["name"])
            pluginClass(self)
            self.printer.debug("{} loaded successfully".format(i["name"]))

    @property
    def getPlugins(self):
        """Gets all plugins in the ./plugins folder

        @return: A list of all found plugins
        @since 0.0.1-beta
        """
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
        """

        @param plugin:
        @return:
        @since 0.0.1-beta
        """
        return imp.load_module(self.mainModule, *plugin["info"])

    def addListener(self, plugin, name, fn):
        """

        @param plugin:
        @param name:
        @param fn:
        @since 0.0.1-beta
        """
        if not plugin in self.pluginFn:
            self.pluginFn.update({plugin: {name: fn}})
        else:
            self.pluginFn[plugin].update({name: fn})
        self.printer.debug("Added method '{}' from plugin '{}'".format(name, plugin))

    def removeListener(self, plugin, name):
        """

        @param plugin:
        @param name:
        @since 0.0.1-beta
        """
        self.pluginFn[plugin].__delitem__(name)
        self.printer.debug("Removed method '{}' from plugin '{}'".format(name, plugin))

    def getListener(self, plugin, name, args, project, variant):
        """

        @param plugin:
        @param name:
        @param args:
        @param project:
        @param variant:
        @since 0.0.1-beta
        """
        if plugin in self.pluginFn:
            self.pluginFn.__getitem__(plugin)["updateCurrentProject"](project)
            self.pluginFn.__getitem__(plugin)["updateCurrentVariant"](project.variant(variant))
            self.pluginFn.__getitem__(plugin)[name](args)
        self.printer.debug("Task {} in plugin {} executed".format(plugin, name))
