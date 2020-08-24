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
        w = w * -1
        dic = {v : w}
        self.allEdges[u].update(dic)
        
    def singleSourceLongestPathUtil(self, node):
        for adjnode in self.allEdges[node]:
            dis = self.distance[node] + self.allEdges[node][adjnode]
            if self.distance[adjnode] > dis:
                self.distance[adjnode] = dis
                self.parent[adjnode] = node
            self.singleSourceLongestPathUtil(adjnode)
                
#             adjnode = 'B'
#             print(self.allEdges[node][adjnode])
        

    def singleSourceLongestPath(self, source):
        
        self.distance[source] = 0
        self.singleSourceLongestPathUtil(source)
        print(self.distance)
        for node in self.nodes:
            self.distance[node] = -1 * self.distance[node]
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
    nodes = ['A', 'B', 'C', 'D', 'E']
    allEdges =[('A', 'B', 1), ('A', 'E', 6), ('A', 'D', 7), ('B', 'C', 2), ('D', 'E', 3), ('D', 'C', 2), ('E', 'B', -1)]
    graph = Graph(nodes)
    for u, v, w in allEdges:
        graph.createGraph(u, v, w)
    graph.singleSourceLongestPath('A')
    graph.path('A')
    graph.path('B')
    graph.path('C')
    graph.path('D')
    graph.path('E')
\
#     print(graph.allEdges)
    
