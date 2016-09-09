from abc import ABCMeta, abstractmethod


class IPlugin(object):
    __metaclass__ = ABCMeta


    def __init__(self, context):
        self.context = context
        self.name = self.getName()

    def addFnListener(self, name, fn):
        """Adds a function with a specific name"""
        self.context.addListener(self.name, name, fn)

    def removeFnListener(self, name):
        """Removes a function with a specific name"""
        self.context.removeListener(self.name, name)

    def addOnChangeListener(self, fn):
        """Adds a change listener"""
        self.context.onChange += fn

    def removeOnChangeListener(self, fn):
        """Removes a change listener"""
        self.context.onChange -= fn

    def addOnScriptChangeListener(self, fn):
        """Adds a change listener"""
        self.context.onScriptChange += fn

    def removeOnScriptChangeListener(self, fn):
        """Removes a change listener"""
        self.context.onScriptChange -= fn

    def addOnDependencyChangeListener(self, fn):
        """Adds a change listener"""
        self.context.onDependencyChange += fn

    def removeOnDependencyChangeListener(self, fn):
        """Removes a change listener"""
        self.context.onDependencyChange -= fn

    def __str__(self):
        """Returns the name of the plugin"""
        return self.name

    @abstractmethod
    def getName(self):
        """Return the name of the plugin"""
        raise NotImplementedError("Class {} doesn't implement registerFn()".format(self.__class__.__name__))

    @abstractmethod
    def register(self):
        """Registers additional functions beside of the predefined"""
        raise NotImplementedError("Class {} doesn't implement registerFn()".format(self.__class__.__name__))


class IBuildPlugin(IPlugin):
    __metaclass__ = ABCMeta
    type = "Build"

    def __init__(self, context):
        super(IBuildPlugin, self).__init__(context)
        self.addFnListener("clean", self.clean)
        self.addFnListener("build", self.build)
        self.register()
        pass

    @abstractmethod
    def clean(self):
        """Gets called when clean-action of the plugin is called"""
        raise NotImplementedError("Class {} doesn't implement registerFn()".format(self.__class__.__name__))

    @abstractmethod
    def build(self, variants):
        """Gets called when build-action of the plugin is called (parameter: variants which should be build)"""
        raise NotImplementedError("Class {} doesn't implement registerFn()".format(self.__class__.__name__))


class ITestPlugin(IPlugin):
    __metaclass__ = ABCMeta
    type = "Test"

    def __init__(self, context):
        super(ITestPlugin, self).__init__(context)
        self.addFnListener("test", self.test)
        self.register()
        pass

    @abstractmethod
    def test(self):
        """Gets called when test-action of the plugin is called"""
        raise NotImplementedError("Class {} doesn't implement registerFn()".format(self.__class__.__name__))


class IMiscPlugin(IPlugin):
    __metaclass__ = ABCMeta
    type = "Misc"

    def __init__(self, context):
        super(IMiscPlugin, self).__init__(context)
        self.register()
        pass
