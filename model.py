import sys
sys.path.append('classes')
import pickle
import os.path
from airport import Airport
from routeappinfo import RouteAppInfo



def setup():
	global rapp
	global airports
	##setup
	##load objects from file
	if os.path.isfile('files/database.p'):
		print('file exists')
		with open('files/database.p', 'rb') as input:
			rapp = pickle.load(input)
		for i in range(len(rapp.connectionslist)):
			print(rapp.connectionslist[i].name)
	else:
		print("error")
		return False


	#build list of just airport names
	airports = []
	for i in range(len(rapp.connectionslist)):
		airports.append(rapp.connectionslist[i].name)
	return True


def getAirports():
	global rapp
	global airports
	return airports

def findRoute(origin, destination):
	print(origin)
	print(destination)
	return True