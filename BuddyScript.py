
class BuddyProject:

    def __init__(self, name, version, parameters, requirements, dependencies, variants):
        """

        @param name:
        @param version:
        @param parameters:
        @param requirements:
        @param dependencies:
        @param variants:
        @since 0.0.1-beta
        """
        self.name = name
        self.version = version
        self.parameters = parameters
        self.requirements = requirements
        self.dependencies = dependencies
        self.variants = variants

        for variant in variants:
            for param in parameters:
                variant.parameters.append(param)


    def __str__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return "Name: {}\n\tVersion: {}\n\tParameters: {}\n\tRequirements: {}\n\tDependencies {}\n\tVariants {}".format(
            self.name, self.version, self.parameters, self.requirements, self.dependencies, self.variants)

    def __repr__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return self.name

    def parameter(self, key):
        """Returns the specific BuddyParameter object for the key
        @param key:
        @rtype: BuddyParameter
        @return:
        @since 0.0.1-beta
        """
        return filter(lambda s: s.key == key, self.parameters)[0]

    def variant(self, name):
        """Returns the specific BuddyVariant object for the name
        @rtype: BuddyVariant
        @since 0.0.1-beta
        """
        return filter(lambda s: s.name == name, self.variants)[0]


class BuddyVariant:

    def __init__(self, name, conditions, parameters):
        """

        @param name:
        @param conditions:
        @param parameters:
        @since 0.0.1-beta
        """
        self.name = name
        self.conditions = conditions
        self.commands = filter(lambda s: ('run' == s.key) or ('before_run' == s.key) or ('after_run' == s.key), parameters)
        self.parameters = filter(lambda s: ('run' != s.key) and ('before_run' != s.key) and ('after_run' != s.key), parameters)

    def __str__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return "Name: {}\n\tConditions: {}\n\tparameters: {}\n\tCommands: {}".format(self.name, self.conditions,
                                                                                 self.parameters, self.commands)

    def __repr__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return self.name

    def command(self, name):
        """

        @param name:
        @return:
        @since 0.0.1-beta
        """
        return filter(lambda s: s.key == name, self.commands)[0]

    def parameter(self, key):
        """

        @param key:
        @return:
        @since 0.0.1-beta
        """
        return filter(lambda s: s.key == key, self.parameters)[0]


class BuddyDependency:

    def __init__(self, service, id):
        """

        @param service:
        @param id:
        @since 0.0.1-beta
        """
        self.service = service
        self.id = id

    def __str__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return self.id

    def __repr__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return self.id


class BuddyRequirement:

    def __init__(self, name):
        """

        @param name:
        @since 0.0.1-beta
        """
        self.name = name

    def __str__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return self.name

    def __repr__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return self.name


class BuddyParameter:

    def __init__(self, key, values):
        """

        @param key:
        @param values:
        @since 0.0.1-beta
        """
        self.key = key
        self.values = values

    def getValuesCount(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return len(self.values)

    def __str__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return self.key

    def __repr__(self):
        """

        @return:
        @since 0.0.1-beta
        """
        return "{} - {}".format(self.key, self.values)


class BuddyPrinter:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    INFO = '\033[93m'
    WARNING = '\e[38;5;208m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self, debug=False):
        """

        @param debug:
        @since 0.0.1-beta
        """
        self.isDebug = debug
        pass

    def setDebug(self, debug):
        """

        @param debug:
        @since 0.0.1-beta
        """
        self.isDebug = debug

    def okay(self, text):
        """

        @param text:
        @since 0.0.1-beta
        """
        print "{}{}{}".format(self.OKGREEN, text, self.ENDC)

    def info(self, text):
        """

        @param text:
        @since 0.0.1-beta
        """
        print "{}{}{}".format(self.OKBLUE, text, self.ENDC)

    def debug(self, text):
        """

        @param text:
        @since 0.0.1-beta
        """
        if self.isDebug:
            print "{}{}{}".format(self.OKBLUE, text, self.ENDC)

    def warning(self, text):
        """

        @param text:
        @since 0.0.1-beta
        """
        print "{}{}{}".format(self.WARNING, text, self.ENDC)

    def error(self, text):
        """

        @param text:
        @since 0.0.1-beta
        """
        print "{}{}{}{}".format(self.FAIL,self.BOLD, text, self.ENDC)
