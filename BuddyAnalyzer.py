import re

from pyparsing import *
from BuddyScript import *


class BuddyAnalyzer:

    varQuoted = QuotedString("'", "\\") | QuotedString('"', '\\')
    varAlphaNumExtra = Word(alphanums + '_')
    varBool = CaselessLiteral('true') | CaselessLiteral('false')
    DELIMITER = CaselessLiteral(':').suppress() | CaselessLiteral('=').suppress()
    LPAREN = CaselessLiteral('(').suppress()
    RPAREN = CaselessLiteral(')').suppress()
    LBRACE = CaselessLiteral('{').suppress()
    RBRACE = CaselessLiteral('}').suppress()
    EOL = CaselessLiteral(';').suppress()
    COMMA = CaselessLiteral(',').suppress()

    assignBrackets = Forward()
    assignDoubleDash = Forward()
    param = assignBrackets | assignDoubleDash | varAlphaNumExtra | varQuoted | varBool
    paramparameters = delimitedList(assignBrackets, '&') | delimitedList(assignDoubleDash,
                                                                         '&') | varAlphaNumExtra | varQuoted | varBool
    assignBrackets << Group(
        varAlphaNumExtra + LPAREN + ZeroOrMore(Group(delimitedList(paramparameters))) + RPAREN + Optional(EOL))
    assignDoubleDash << Group(varAlphaNumExtra + DELIMITER + Group(paramparameters) + Optional(EOL))

    keywordRequirements = CaselessKeyword('requires').suppress()
    keywordName = CaselessKeyword('name').suppress()
    keywordVersion = CaselessKeyword('version').suppress()
    keywordVariant = CaselessKeyword('variant').suppress()
    keywordDependencies = CaselessKeyword('dependencies').suppress()

    requirements = keywordRequirements + DELIMITER + delimitedList(varQuoted)('requirements') + Optional(EOL)
    name = keywordName + DELIMITER + varQuoted('name') + Optional(EOL)
    version = keywordVersion + DELIMITER + varQuoted('version') + Optional(EOL)
    variant = Group(keywordVariant + varAlphaNumExtra('name') + Optional(
        LPAREN + delimitedList(OneOrMore(assignDoubleDash))('conditions') + RPAREN) + LBRACE + Optional(
        delimitedList(OneOrMore(param)))('parameters') + RBRACE + Optional(EOL))
    dependencies = keywordDependencies + LBRACE + Optional(
        delimitedList(Group(varAlphaNumExtra('service') + varQuoted('id')))('dependencies')) + RBRACE + Optional(EOL)

    parser = Group(requirements)('requirements') + Group(name + version)('meta') + delimitedList(
        ZeroOrMore(assignBrackets))('parameters') + Dict(Group(OneOrMore(variant))('variants')) + dependencies

    def __init__(self, debug, file):
        """ Creates a new BuddyAnalyzer

        @param debug: True -> Show debug msgs
        @param file: The complete path to the script
        @since 0.0.1-beta
        """
        self.printer = BuddyPrinter(debug)
        self.file = file

    def analyze(self):
        """Analyzes the script file

        @note: Exits when the file syntax is wrong
        @return: A BuddyProject with the complete parsed elements
        @since 0.0.1-beta
        """
        self.printer.debug("Starting analyzing script")
        lines = open(self.file)
        script = self.removeComments(lines.read())
        try:
            res = self.parser.parseString(script)
        except ParseException:
            self.printer.error("Parser error. Please check if the element order and the syntax is correct")
            exit()
        parameters = []
        for elem in res.parameters:
            parameters.append(BuddyParameter(elem[0], elem[1]))
        requirements = []
        for elem in res.requirements:
            requirements.append(BuddyRequirement(elem))
        dependencies = []
        for elem in res.dependencies:
            dependencies.append(BuddyDependency(elem.service, elem.id))
        variants = []
        for elem in res.variants:
            params = []
            for param in elem.parameters:
                params.append(BuddyParameter(param[0], param[1]))
            variants.append(BuddyVariant(elem.name, elem.conditions, params))
        self.printer.debug("Finished analyzing script")
        return BuddyProject(res.meta.name, res.meta.version, parameters, requirements, dependencies, variants)

    @staticmethod
    def removeComments(string):
        """Removes all Comments (TODO: Check for best comment indicator)

        @param string: The string with comments
        @return: The string without the comments
        @since 0.0.1-beta
        """
        string = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", string)  # remove all java-like multi-line comments
        string = re.sub(re.compile("//.*?\n"), "", string)  # remove all java-like single line comments
        string = re.sub(re.compile("\#.*?\n"), "", string) # remove all python like comments
        return string
