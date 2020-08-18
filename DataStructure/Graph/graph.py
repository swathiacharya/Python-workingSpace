'''  GRAPH can be represented
        1=> Adjacency Matrix :
                Pros: Easy to check whether there is the relation between two node
                      Easy to implemenet
                      Removing an edge take O(1)

                Cons: Consume more Space O(V^2)
                      adding vertex is O(V^2) time
        2=> Adjacency MAtrix
                An array  of list is used.
                The size of the array is equal to the  number of Vertices
'''
# Adjacency Matrix

# class of the adjency list of the node


'''
|A| --> [B, C]
|B| --> [A, D]
|C| --> [A, D, E]
|D| --> [B, C, E]
|E| --> [C, D]
'''


# USING DISCTIONARY AND LIST

class Graph:
    def __init__(self,Nodes, isDirected = False):  # nodes : {}
        self.nodes = Nodes
        self.adj_list = {}
        self.isDirected = isDirected
        for node in self.nodes:
            self.adj_list[node]=[]
        '''
        |A| --> []
        |B| --> []
        |C| --> []
        |D| --> []
        |E| --> []
       '''
    def addEdge(self, u, v):
        self.adj_list[u].append(v)
        if  not self.isDirected:
            self.adj_list[v].append(u)

    def printGraph(self):
        for node in self.nodes:
            print('{} ---> {} '.format(node,self.adj_list[node]))
    '''
    For Undirected graph
    A ---> ['B', 'E']
    B ---> ['A', 'E', 'D', 'C']
    C ---> ['B', 'D']
    D ---> ['B', 'C', 'E']
    E ---> ['A', 'B', 'D']
    
    Directed
    A ---> ['B', 'E']
    B ---> ['E', 'D', 'C']
    C ---> ['D']
    D ---> ['E']
    E ---> []

    '''



if __name__ == "__main__":
    nodeValue = ['A', 'B', 'C', 'D', 'E']
    allEdges = [('A', 'B'),('A','E'),('B','E'), ('B','D'), ('B','C'), ('C', 'D') ,('D','E')]
    graph = Graph(nodeValue, isDirected = True)
    # graph.addEdge('A','B')
    for u,v in allEdges:
        graph.addEdge(u, v)
    graph.printGraph()
    