class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]