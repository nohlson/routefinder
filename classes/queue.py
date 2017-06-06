class Queue:
	def __init__():
		self.queue = []

	def enqueue(self, val):
		self.queue.append(val)

	def dequeue(self):
		val = self.queue[0]
		if len(self.queue) == 1:
			self.queue = []
		else:
			self.queue = self.queue[1:]

		return val

	def isEmpty(self):
		if (len(self.queue) == 0):
			return True
		else:
			return False