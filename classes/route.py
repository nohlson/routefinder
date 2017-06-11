class Route:

    def __init__(self, startLocation):
        self.__path = [startLocation]
        self.__distance = 0

    def addAirport(self, newAirport):
        tempConnections = self.__path[-1].getConnections()
        for i in range(len(tempConnections)):
            if tempConnections[i].getAirport().getCode() == newAirport.getCode():
                self.__distance += tempConnections[i].getDistance()
                self.__path.append(newAirport)
                return True
        return False

    def getPath(self):
        return self.__path

    def getDistance(self):
        return self.__distance

    def getDistanceMiles(self):
        return self.__distance * 0.000621371