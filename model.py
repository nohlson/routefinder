import sys
sys.path.append('classes')
import pickle
import os.path
from airport import Airport
from routeappinfo import RouteAppInfo
from aqueue import AQueue
from copy import deepcopy


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
			for j in range(len(rapp.connectionslist)):
				if rapp.connectionslist[i].name == rapp.connectionslist[j].name and i != j:
					print("duplicate")
			print(rapp.connectionslist[i].name)
	else:
		print("error")
		return False


	#build list of just airport names
	airports = []
	for i in range(len(rapp.connectionslist)):
		airports.append(rapp.connectionslist[i].name)
	return True

def BFS(graph, start, end, q):

	temp_path = [start]
	valid_paths=[[]]
	numValidPaths = 0
	maxCycles = 80000
	cycleNum = 0;

	q.enqueue(temp_path)
	sys.stdout.write("Working...")
	while not q.isEmpty():
		if cycleNum >= maxCycles:
			break
		temp_path = q.dequeue()
		last_node = temp_path[len(temp_path)-1]
		# for i in temp_path:
		# 	sys.stdout.write(i.name + " ->")
		# sys.stdout.write("\n")
		if last_node.name == end.name:
			numValidPaths += 1
			# sys.stdout.write("Valid path: ")
			new_temp = deepcopy(temp_path)
			valid_paths.append(new_temp)
			# for i in temp_path:
			# 	sys.stdout.write(i.name + " ->")
			# sys.stdout.write("\n")
			if numValidPaths > 10:
				return valid_paths
		for link_node in range(len(last_node.connections)):
			newLinkFoundInPath = False
			for k in range(len(temp_path)):
				if last_node.connections[link_node].name == temp_path[k].name:
					newLinkFoundInPath = True
					break
			if not newLinkFoundInPath:
				new_path = temp_path + [last_node.connections[link_node]]
				q.enqueue(new_path)
		cycleNum += 1
		if cycleNum % 10000 == 0:
			print(cycleNum)
	sys.stdout.write("Done")
	return valid_paths


def getAirports():
	global rapp
	global airports
	return airports


def findRoute(origin, destination):
	print(origin)
	print(destination)
	q = AQueue()
	#find origin and destination airports
	for i in range(len(rapp.connectionslist)):
		if rapp.connectionslist[i].name == origin:
			originAP = rapp.connectionslist[i]
			break
	for i in range(len(rapp.connectionslist)):
		if rapp.connectionslist[i].name == destination:
			destAP = rapp.connectionslist[i]
			break
	return BFS(rapp.connectionslist, originAP, destAP, q)

	