class Airport:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def addConnection(self, connect):
        self.connections.append(connect)

    def hasConnection(self, connect):
        for i in self.connections:
            if connect == i.name:
                return True

        return False