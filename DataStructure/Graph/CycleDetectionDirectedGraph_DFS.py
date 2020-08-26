class Graph:
    def __init__(self, node):
        self.nodes = node
        self.allEdge = dict()
        self.parent = dict()
        self.visited = dict()
        self.count = 0
        self.stack = []
        self.printArr = []
        
        for node in self.nodes:
            self.allEdge[node] = []
            self.parent[node] = -1
            self.visited[node] = -1
            self.flagCycle = False
            
    def createGraph(self, u, v):
        if u == v:
            self.count = self.count + 1
            self.flagCycle = True
        else:
            self.allEdge[u].append(v)
    
    def path(self, node, adjNodeRep):
        self.printArr.append(adjNodeRep)
        v = node
        while v  not in self.printArr:
            self.printArr.append(v)
            v = self.parent[v]
        self.printArr.reverse()
        print('{} --->'.format(adjNodeRep),end = '')
        for node in self.printArr:
            print('{} --->'.format(node),end = '')
        print('Cyclic',self.count)
        self.printArr.clear()

            
    def cycleDetectionDirectedUtil(self,node):
        for adjnode in self.allEdge[node]:

            if self.visited[adjnode] == -1:
                self.visited[adjnode] = 0
                self.stack.append(adjnode)
                self.parent[adjnode] = node
                self.cycleDetectionDirectedUtil(adjnode)
            elif self.visited[adjnode] == 0:
                self.flagCycle = True
                self.count = self.count + 1
                self.path(node, adjnode)
                 
        else:            
            self.visited[self.stack.pop()] = 1
               
                
    def cycleDetectionDirected(self):
        for node in self.nodes:
            s= node
            self.parent[s] = None
            self.visited[s] = 0
            self.stack.append(s)
            self.cycleDetectionDirectedUtil(s)
        if self.flagCycle:
            print("CYCLIC")
            print(self.count)
        else:
            print("ACYCLIC")
if __name__ == '__main__':
    node = ['A', 'B', 'C', 'D','E']
#     allEdge = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('D','B')]
    allEdge = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('D', 'E'), ('E', 'B'), ('C', 'A')]
#     allEdge = [('A', 'B'), ('B', 'C'), ('B', 'D'),('C', 'A'),('C', 'D'),('C', 'E'),('D', 'E'),('E', 'B')]
    graph = Graph(node)
    
    for u, v in allEdge:
        graph.createGraph(u,v)
    graph.cycleDetectionDirected()
