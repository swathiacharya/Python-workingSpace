class Graph:
    def __init__(self, node):
        self.nodes = node
        self.allEdge = dict()
        self.parent = dict()
        self.visited = dict()
        self.count = 0
        
        for node in self.nodes:
            self.allEdge[node] = []
            self.parent[node] = -1
            self.visited[node] = False
            self.flagCycle = False
        
    def createGraph(self, u, v):
        self.allEdge[u].append(v)
        self.allEdge[v].append(u)
            
    def cycleDetectionUndirectedUtil(self,node):        
        for adjNode in self.allEdge[node]:            
            if not self.visited[adjNode]:
                self.visited[adjNode] = True
                self.parent[adjNode] = node
                self.cycleDetectionUndirectedUtil(adjNode)
            elif adjNode is not self.parent[node]:
                self.flagCycle = True
                self.count = self.count + 1
                
               
                
    def cycleDetectionUndirected(self):
        s = 'A'
        self.visited[s] = True
#         self.parent[s] = 'A'
        for node in self.nodes:
            if node in self.allEdge[node]:
                self.flagCycle = True
                print(self.flagCycle)
                break
        self.cycleDetectionUndirectedUtil(s)
        if(self.flagCycle):
            print('CYCLE IS PRESENT')
            print(self.count // 2)
        else:
            print('CYCLE IS Not PRESENT')     
if __name__ == '__main__':
    node = ['A', 'B', 'C', 'D']
#     allEdge = [('A', 'B'), ('A', 'C'), ('C', 'D'), ('D','A'),('B', 'C'), ('B', 'D')]
#     node = ['A', 'B', 'C', 'D','E']
#     allEdge = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
    allEdge = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A','D')]
    
    graph = Graph(node)
    for u, v in allEdge:
        graph.createGraph(u,v)
    graph.cycleDetectionUndirected()
        
        
