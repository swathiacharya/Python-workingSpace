#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjEdge = dict()
        self.visited = dict()
        self.dfsResult = []
        self.parent = dict()
        for node in self.nodes:
            self.adjEdge[node] =[]
            self.visited[node] = False
            self.parent[node] = []
            
    def dfs(self, source):
        if self.visited[source]:
            return
        else:
            self.visited[source] = True
            self.dfsResult.append(source)
            
            for v in self.adjEdge[source]:
                self.parent[v].append(source)
                self.dfs(v)
            
        
        
            
    def addEdge(self, u, v):
        self.adjEdge[u].append(v)
        
    


# In[33]:


if __name__ == '__main__':
#     nodes = ['A', 'B', 'C', 'D']
#     allEdge = [('A','B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
    nodes = [0, 1, 2, 3]
    allEdge = [(0,1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    graph = Graph(nodes)
    
    for u, v in allEdge:
        graph.addEdge(u, v)
    graph.dfs(1)
    print(graph.dfsResult)
    print(graph.parent)


# In[ ]:




