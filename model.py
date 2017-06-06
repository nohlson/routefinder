import _pickle as pickle
import os.path



def setup():
	##setup
	##load objects from file
	if os.path.isfile('files/database.p'):
		print('file exists')
	else:
		print("error")
		return False


	return True


def getAirports():


	return ['LAX', 'MIA']



def findRoute(origin, destination):
	print(origin)
	print(destination)
	return True