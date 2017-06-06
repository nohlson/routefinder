import sys
sys.path.append('../classes')
import openpyxl
from airport import Airport
from routeappinfo import RouteAppInfo
import  pickle


def bubbleSort(connections): ##dont care how slow it is
    for passnum in range(len(connections)-1,0,-1):
        for i in range(passnum):
            if connections[i].name >connections[i+1].name:
                temp = connections[i]
                connections[i] = connections[i+1]
                connections[i+1] = temp



airports = []


wb = openpyxl.load_workbook('Markets.xlsx')

sheet = wb.get_sheet_by_name('Sheet1')
print("Number of entries: " + str(sheet.max_row))

for i in range(2,sheet.max_row+1):
    airportName = str(sheet.cell(column=1, row=i).value)
    connectionName = str(sheet.cell(column=2, row=i).value)
    print(str(airportName) + " connect to " + str(connectionName))
    airportFoundInList = False
    for j in range(len(airports)): ##go through airports
        if airportName == airports[j].name: #if new airport exists in working database
            print("    Found origin airport in database")
            airportFoundInList = True
            if not airports[j].hasConnection(connectionName): #if the connection doesn't already exist
                print("    Connection doesn't already exist")
                connectionExistsAsAirport = False
                for k in range(len(airports)):
                    if connectionName == airports[k].name:
                        print("    Found dest in database")
                        airports[j].addConnection(airports[k])
                        airports[k].addConnection(airports[j])
                        connectionExistsAsAirport = True
                        break
                if not connectionExistsAsAirport:
                    print("    Creating new airport and adding it")
                    tempAir = Airport(connectionName)
                    tempAir.addConnection(airports[j])
                    airports[j].addConnection(tempAir)
                    airports.append(tempAir)
            else:
                print("    Connection already exists")
            break
    if not airportFoundInList:
        print("    Origin airport not found in database, adding to list and creating connection")
        tempAir = Airport(airportName)
        foundDestinationInList = False
        for j in range(len(airports)):
            if connectionName == airports[j].name:
                print("    Found destination in database")
                foundDestinationInList = True
                tempAir.addConnection(airports[j])
                airports[j].addConnection(tempAir)
                break
        if not foundDestinationInList:
            print("    Dest not found in databse, creating and adding it")
            tempAirDest = Airport(connectionName)
            tempAirDest.addConnection(tempAir)
            tempAir.addConnection(tempAirDest)
            airports.append(tempAirDest)

        airports.append(tempAir)
    
bubbleSort(airports)

for i in range(len(airports)):
    for j in range(len(airports)):
        if airports[i].name == airports[j].name and i != j:
            print("Duplicate")


for i in range(len(airports)):
    print("Airport: " + airports[i].name)
    for j in range(len(airports[i].connections)):
       print("    Connection to: " + airports[i].connections[j].name)



rapp = RouteAppInfo(airports)
with open('../files/database.p', 'wb') as output:
    pickle.dump(rapp, output, pickle.HIGHEST_PROTOCOL)