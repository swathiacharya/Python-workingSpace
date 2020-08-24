class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.allEdges = dict()
        self.visited = dict()
        self.arr = []
        self.stack = []
        
        for node in self.nodes:
            self.allEdges[node] = []
            self.parent = None
            self.visited[node] = False
            
            
    def topologicalUtil(self, node):
        if not self.visited[node]:
            self.visited[node] = True
            self.stack.append(node)
            for adjnode in self.allEdges[node]:
                    self.topologicalUtil(adjnode)
            else:
                pop = self.stack.pop()
                self.arr.append(pop)
                return
            
        
            
    def topologicalSort(self):
        for node in self.nodes:
            self.topologicalUtil(node)
        self.arr.reverse()
        print(self.arr)
            
    def createGraph(self, u, v):
        self.allEdges[u].append(v)
        


if __name__ == '__main__':
#     nodes = ['A', 'B', 'C']
#     allEdges = [('A','C'), ('B','C')]
#     nodes = ['A', 'B', 'C', 'D', 'E']
#     allEdges = [('A','C'), ('B','C'), ('B','D'), ('C','E'), ('D','E')]
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    allEdges = [('C', 'D'), ('D', 'B'), ('F', 'A'), ('F', 'C'), ('E', 'A'), ('E', 'B'), ]
    graph = Graph(nodes)
    for u, v in allEdges:
        graph.createGraph(u,v)
    graph.topologicalSort()
