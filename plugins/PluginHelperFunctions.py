"""File which contains useful functions for plugins"""

def isTrue(str):
    """Checks for yes, true, t and 1

    @param str: The string containing a bool expression
    @return: A bool object
    @since 0.0.1-beta
    """
    return str in ("yes", "true", "t", "1")


def isFalse(str):
    """Checks for no, false, f and 0

    @param str: The string containing a bool expression
    @return: A bool object
    @since 0.0.1-beta
    """
    return str in ("no", "false", "f", "0")
