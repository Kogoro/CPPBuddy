from abc import ABCMeta, abstractmethod

from BuddyScript import BuddyPrinter


class IPlugin(object):
    __metaclass__ = ABCMeta

    def __init__(self, context):
        """

        @param context:
        @since 0.0.1-beta
        """
        self.printer = BuddyPrinter()
        self.context = context
        self.name = self.getName()

    def addFnListener(self, name, fn):
        """Adds a function with a specific name
        @param name:
        @param fn:
        @since 0.0.1-beta
        """
        self.context.addListener(self.name, name, fn)

    def removeFnListener(self, name):
        """Removes a function with a specific name
        @param name:
        @since 0.0.1-beta
        """
        self.context.removeListener(self.name, name)

    def addOnChangeListener(self, fn):
        """Adds a change listener
        @param fn:
        @since 0.0.1-beta
        """
        self.context.onChange += fn

    def removeOnChangeListener(self, fn):
        """Removes a change listener
        @param fn:
        @since 0.0.1-beta
        """
        self.context.onChange -= fn

    def addOnScriptChangeListener(self, fn):
        """Adds a change listener
        @param fn:
        @since 0.0.1-beta
        """
        self.context.onScriptChange += fn

    def removeOnScriptChangeListener(self, fn):
        """Removes a change listener
        @param fn:
        @since 0.0.1-beta
        """
        self.context.onScriptChange -= fn

    def addOnDependencyChangeListener(self, fn):
        """Adds a change listener
        @param fn:
        @since 0.0.1-beta
        """
        self.context.onDependencyChange += fn

    def removeOnDependencyChangeListener(self, fn):
        """Removes a change listener
        @param fn:
        @since 0.0.1-beta
        """
        self.context.onDependencyChange -= fn

    def updateCurrentProject(self, project):
        """Updates the current project object
        @param project:
        @since 0.0.1-beta
        """
        self.curProject = project

    def updateCurrentVariant(self, variant):
        """Updates the current variant object
        @param variant:
        @since 0.0.1-beta
        """
        self.curVariant = variant

    def __str__(self):
        """Returns the name of the plugin
        @return:
        @since 0.0.1-beta
        """
        return self.name

    @abstractmethod
    def getName(self):
        """Return the name of the plugin
        @rtype: String
        @since 0.0.1-beta
        """
        raise NotImplementedError("Class {} doesn't implement getName(self)".format(self.__class__.__name__))

    @abstractmethod
    def register(self):
        """Registers additional functions beside of the predefined
        @rtype: String
        @since 0.0.1-beta
        """
        raise NotImplementedError("Class {} doesn't implement register(self)".format(self.__class__.__name__))


class IBuildPlugin(IPlugin):
    __metaclass__ = ABCMeta
    type = "Build"

    def __init__(self, context):
        """

        @param context:
        @since 0.0.1-beta
        """
        super(IBuildPlugin, self).__init__(context)
        self.addFnListener("updateCurrentProject", self.updateCurrentProject)
        self.addFnListener("updateCurrentVariant", self.updateCurrentVariant)
        self.addFnListener("clean", self.clean)
        self.addFnListener("build", self.build)
        self.register()
        pass

    @abstractmethod
    def clean(self, args):
        """Gets called when clean-action of the plugin is called
        @param args:
        @since 0.0.1-beta
        """
        raise NotImplementedError("Class {} doesn't implement clean(self, args)".format(self.__class__.__name__))

    @abstractmethod
    def build(self, args):
        """Gets called when build-action of the plugin is called (parameter: variants which should be build)
        @param args:
        @since 0.0.1-beta
        """
        raise NotImplementedError("Class {} doesn't implement build(self, args)".format(self.__class__.__name__))


class ITestPlugin(IPlugin):
    __metaclass__ = ABCMeta
    type = "Test"

    def __init__(self, context):
        """

        @param context:
        @since 0.0.1-beta
        """
        super(ITestPlugin, self).__init__(context)
        self.addFnListener("updateCurrentProject", self.updateCurrentProject)
        self.addFnListener("updateCurrentVariant", self.updateCurrentVariant)
        self.addFnListener("test", self.test)
        self.register()
        pass

    @abstractmethod
    def test(self, args):
        """Gets called when test-action of the plugin is called
        @param args:
        @since 0.0.1-beta
        """
        raise NotImplementedError("Class {} doesn't implement test(self, args)".format(self.__class__.__name__))


class IMiscPlugin(IPlugin):
    __metaclass__ = ABCMeta
    type = "Misc"

    def __init__(self, context):
        """

        @param context:
        @since 0.0.1-beta
        """
        super(IMiscPlugin, self).__init__(context)
        self.addFnListener("updateCurrentProject", self.updateCurrentProject)
        self.addFnListener("updateCurrentVariant", self.updateCurrentVariant)
        self.addFnListener("run", self.run)
        self.register()
        pass

    @abstractmethod
    def run(self, args):
        """Gets called when no action of the plugin is specified
        @param args:
        @since 0.0.1-beta
        """
        raise NotImplementedError("Class {} doesn't implement run(self, args)".format(self.__class__.__name__))
