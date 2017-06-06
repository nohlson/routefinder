class airport:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def addConnection(self, connect):
        self.connections.add(connect)