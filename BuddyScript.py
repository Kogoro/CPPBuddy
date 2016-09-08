
class BuddyProject:

    def __init__(self, name, version, parameters, requirements, dependencies, variants):
        self.name = name
        self.version = version
        self.parameters = parameters
        self.requirements = requirements
        self.dependencies = dependencies
        self.variants = variants

    def __str__(self):
        return "Name: {}\n\tVersion: {}\n\tParameters: {}\n\tRequirements: {}\n\tDependencies {}\n\tVariants {}".format(
            self.name, self.version, self.parameters, self.requirements, self.dependencies, self.variants)

    def __repr__(self):
        return self.name

    def parameter(self, key):
        return str(filter(lambda s: s.key == key, self.parameters)[0])

    def variant(self, name):
        return filter(lambda s: s.name == name, self.variants)[0]


class BuddyVariant:

    def __init__(self, name, conditions, parameters):
        self.name = name
        self.conditions = conditions
        self.commands = filter(lambda s: ('run' == s.key) or ('before_run' == s.key) or ('after_run' == s.key), parameters)
        self.parameters = filter(lambda s: ('run' != s.key) and ('before_run' != s.key) and ('after_run' != s.key), parameters)

    def __str__(self):
        return "Name: {}\n\tConditions: {}\n\tparameters: {}\n\tCommands: {}".format(self.name, self.conditions,
                                                                                 self.parameters, self.commands)

    def __repr__(self):
        return self.name

    def command(self, name):
        return filter(lambda s: s.key == name, self.commands)[0]


class BuddyDependency:

    def __init__(self, service, id):
        self.service = service
        self.id = id

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id


class BuddyRequirement:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class BuddyParameter:

    def __init__(self, key, values):
        self.key = key
        self.values = values

    def getValuesCount(self):
        return len(self.values)

    def __str__(self):
        return self.key

    def __repr__(self):
        return "{} - {}".format(self.key, self.values)