import sys
import pickle
import os.path
from airport import Airport
from routeappinfo import RouteAppInfo
from aqueue import AQueue
from copy import deepcopy


class Model:

	def __init__(self):
		self.airports = None
		self.rapp = None
		self.g2g = self.setup()

	def setup(self):
		##setup
		##load objects from file
		if os.path.isfile('files/database.p'):
			print('file exists')
			with open('files/database.p', 'rb') as input:
				self.rapp = pickle.load(input)
			for i in range(len(self.rapp.connectionslist)):
				for j in range(len(self.rapp.connectionslist)):
					if self.rapp.connectionslist[i].name == self.rapp.connectionslist[j].name and i != j:
						print("duplicate")
				print(self.rapp.connectionslist[i].name)
		else:
			print("error")
			return False


		#build list of just airport names
		self.airports = []
		for i in range(len(self.rapp.connectionslist)):
			self.airports.append(self.rapp.connectionslist[i].name)
		return True

	def BFS(self, graph, start, end, q):

		temp_path = [start]
		valid_paths=[[]]
		numValidPaths = 0
		maxCycles = 80000
		maxValidPaths = 300
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
				if numValidPaths > maxValidPaths:
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


	def getAirports(self):
		return self.airports


	def findRoute(self, origin, destination):
		print(origin)
		print(destination)
		q = AQueue()
		#find origin and destination self.airports
		for i in range(len(self.rapp.connectionslist)):
			if self.rapp.connectionslist[i].name == origin:
				originAP = self.rapp.connectionslist[i]
				break
		for i in range(len(self.rapp.connectionslist)):
			if self.rapp.connectionslist[i].name == destination:
				destAP = self.rapp.connectionslist[i]
				break
		return self.BFS(self.rapp.connectionslist, originAP, destAP, q)


	def verifySetup(self):
		return self.g2g
		