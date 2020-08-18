'''
BFS using queue with list and dictionary
'''


from queue import Queue;


class Graph:
    def __init__(self,Nodes,isDirected = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.isDirected = isDirected
        for node in self.nodes:
            self.adj_list[node] = []

    def addEdges(self, u, v):
        self.adj_list[u].append(v)
        if not self.isDirected:
            self.adj_list[v].append(u)

    def printGraph(self):
        for node in self.nodes:
            print('{} --> {}'.format(node, self.adj_list[node]))

    def BFS_Utility(self):
        
        visited = {}
        parent = {}
        level = {}
        path =[]
        bfsOutput = []
        queue = Queue()
        #
        for node in self.nodes:
            level[node] = -1
            visited[node] = False
            parent[node] = None
        
        src = 'A'
        visited[src] = True
        level[src] = 0
        queue.put(src)
        while not queue.empty():
            u = queue.get()
            bfsOutput.append(u)
            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    level[v] = level[u] + 1
                    queue.put(v)
        print(visited)
        print(parent)
        print(level)
        print(bfsOutput)
        dest = input()
        while dest is not None:
            path.append(dest)
            dest = parent[dest]
        print(path)
        path.reverse()
        print(path)
        
                    
                    
            
            
        




if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E']
    # nodes = []
    # print("number of nodes")
    # for n in range(int(input())):
    #     print('Enter the Name of Node {}'.format(n+1))
    #     nodes.append(input())
    graph = Graph(nodes,isDirected= False)
    allEdges = [('A', 'B'),('A','E'),('B','E'), ('B','D'), ('B','C'), ('C', 'D') ,('D','E')]
    for u, v in allEdges:
        graph.addEdges(u, v)
    
    graph.printGraph()
    graph.BFS_Utility()
    