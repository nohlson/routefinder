class Airport:
    def __init__(self, code):
        self.__code = code
        self.__connections = []
        self.__name = None
        self.__city = None
        self.__country = None
        self.__latitude = None
        self.__longitude = None

    def addConnection(self, connect):
        self.__connections.append(connect)

    def getCode(self):
        return self.__code

    def setCode(self, code):
        self.__code = code

    def hasConnection(self, connect):
        for i in self.__connections:
            if connect == i.getAirport().getCode():
                return True

        return False

    def getConnections(self):
        return self.__connections

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getCity(self):
        return self.__city

    def setCity(self, newCity):
        self.__city = newCity

    def getCountry(self):
        return self.__country

    def setCountry(self, newCountry):
        self.__country = newCountry

    def getLatitude(self):
        return self.__latitude

    def setLatitude(self, newLatitude):
        self.__latitude = newLatitude

    def getLongitude(self):
        return self.__longitude

    def setLongitude(self, newLongitude):
        self.__longitude = newLongitude


