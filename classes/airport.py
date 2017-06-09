class Airport:
    def __init__(self, code):
        self.__code = code
        self.__connections = []

    def addConnection(self, connect):
        self.__connections.append(connect)

    def getCode(self):
        return self.__code

    def setCode(self, code):
        self.__code = code

    def hasConnection(self, connect):
        for i in self.__connections:
            if connect == i.getCode():
                return True

        return False

    def getConnections(self):
        return self.__connections