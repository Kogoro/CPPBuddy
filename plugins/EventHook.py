class EventHook(object):

    def __init__(self):
        """
        @since 0.0.1-beta
        """
        self.__handlers = []

    def __iadd__(self, handler):
        """

        @param handler:
        @return:
        @since 0.0.1-beta
        """
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        """

        @param handler:
        @return:
        @since 0.0.1-beta
        """
        self.__handlers.remove(handler)
        return self

    def fire(self, *args, **keywargs):
        """

        @param args:
        @param keywargs:
        @since 0.0.1-beta
        """
        for handler in self.__handlers:
            handler(*args, **keywargs)

    def clearObjectHandlers(self, inObject):
        """

        @param inObject:
        @since 0.0.1-beta
        """
        for theHandler in self.__handlers:
            if theHandler.im_self == inObject:
                self -= theHandler

