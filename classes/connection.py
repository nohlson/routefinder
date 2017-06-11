class Connection:
    def __init__(self, airport):
        self.__airport = airport
        self.__distance = None

    def setDistance(self, newDistance):
        self.__distance = newDistance

    def getDistance(self):
        return self.__distance

    def getAirport(self):
        return self.__airport