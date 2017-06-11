import sys
import pickle
import os.path
from aqueue import AQueue
from copy import deepcopy


class Model:
    def __init__(self):
        self.__airportCodes = None
        self.rapp = None
        self.g2g = self.setup()

    def setup(self):
        ##setup
        ##load objects from file
        if os.path.isfile('files/database.p'):
            print('file exists')
            with open('files/database.p', 'rb') as input:
                self.rapp = pickle.load(input)
        else:
            print("error")
            return False

        # build list of just airport names
        self.__airportCodes = []
        for i in range(len(self.rapp.airports)):
            self.__airportCodes.append(self.rapp.airports[i].getCode())
        return True

    def BFS(self, graph, start, end, q, numRoutes):

        temp_path = [start]
        valid_paths = [[]]
        numValidPaths = 0
        maxCycles = 80000
        cycleNum = 0

        q.enqueue(temp_path)
        sys.stdout.write("Working...")
        while not q.isEmpty():
            if cycleNum >= maxCycles:
                break
            temp_path = q.dequeue()
            last_node = temp_path[len(temp_path) - 1]
            # for i in temp_path:
            # 	sys.stdout.write(i.getCode() + " ->")
            # sys.stdout.write("\n")
            if last_node.getCode() == end.getCode():
                numValidPaths += 1
                sys.stdout.write("Valid path: ")
                new_temp = deepcopy(temp_path)
                valid_paths.append(new_temp)
                # for i in temp_path:
                # 	sys.stdout.write(i.getCode() + " ->")
                # sys.stdout.write("\n")
                if numValidPaths > numRoutes:
                    return valid_paths
            lastNodeConnections = last_node.getConnections()
            for link_node in range(len(lastNodeConnections)):
                newLinkFoundInPath = False
                for k in range(len(temp_path)):
                    if lastNodeConnections[link_node].getAirport().getCode() == temp_path[k].getCode():
                        newLinkFoundInPath = True
                        break
                if not newLinkFoundInPath:
                    new_path = temp_path + [lastNodeConnections[link_node].getAirport()]
                    q.enqueue(new_path)
            cycleNum += 1
            if cycleNum % 10000 == 0:
                print(cycleNum)
        sys.stdout.write("Done")
        return valid_paths

    def getAirportCodes(self):
        return self.__airportCodes

    def findRoute(self, origin, destination, numRoutes):
        print(origin)
        print(destination)
        q = AQueue()
        # find origin and destination self.airports
        for i in range(len(self.rapp.airports)):
            if self.rapp.airports[i].getCode() == origin:
                originAP = self.rapp.airports[i]
                break
        for i in range(len(self.rapp.airports)):
            if self.rapp.airports[i].getCode() == destination:
                destAP = self.rapp.airports[i]
                break
        return self.BFS(self.rapp.airports, originAP, destAP, q, numRoutes)

    def verifySetup(self):
        return self.g2g
