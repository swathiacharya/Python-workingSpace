class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.allEdges = dict()
        self.parent = dict()
        
        self.distance = dict()
        
        for node in self.nodes:
            self.allEdges[node] = {}
            self.parent[node] = None
            self.distance[node] = 999
            

    def createGraph(self, u, v, w):
        dic = {v : w}
        self.allEdges[u].update(dic)
        
    def singleSourceShortestPathUtil(self, node):
        for adjnode in self.allEdges[node]:
            dis = self.distance[node] + self.allEdges[node][adjnode]
            if self.distance[adjnode] > dis:
                self.distance[adjnode] = dis
                self.parent[adjnode] = node
            self.singleSourceShortestPathUtil(adjnode)
                
#             adjnode = 'B'
#             print(self.allEdges[node][adjnode])
        

    def singleSourceShortestPath(self, source):
        
        self.distance[source] = 0
        self.singleSourceShortestPathUtil(source)
        print(self.distance)
        print(self.parent)
        
    def path(self, to):
        v = to
        arr =[]
        while v is not None:
            arr.append(v)
            v = self.parent[v]
        arr.reverse()
        for node in arr:
            print('{} ---> '.format(node), end ='')
        print('* End *')
        
        
        
if  __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    allEdges =[('A', 'B', 3), ('A', 'C', 6), ('B', 'C', 4), ('B','D',4), ('B','E',11), ('C','D',8), ('C','G',11), ('D','E',-4), ('D','F',5), ('D','G',2), ('E','H',9), ('F','H',1), ('G','H',2)]
#     allEdges = [('A', 'C', 5), ('A', 'B', 6), ('B', 'E', 9), ('C', 'B', 2), ('C', 'D', 4), ('D', 'F', -1), ('D', 'G', 1), ('D', 'E', 12), ('F', 'H', 0), ('F', 'G', 1), ('G', 'E', 1), ('G', 'H', 2)]
    graph = Graph(nodes)
    for u, v, w in allEdges:
        graph.createGraph(u, v, w)
    graph.singleSourceShortestPath('A')
    graph.path('A')
    graph.path('B')
    graph.path('C')
    graph.path('D')
    graph.path('E')
    graph.path('F')
    graph.path('G')
    graph.path('H')
#     print(graph.allEdges)
    
