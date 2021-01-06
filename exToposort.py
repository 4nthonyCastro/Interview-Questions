# ====================================
#
# Topological Sort Recursive Example
#
# ====================================

from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        # Dictionary Continued
        self.graph = defaultdict(list)
        # Number of vertices
        self.V = vertices 
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Recursive Function used by Topological Sort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited. 
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False: 
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # This function does the Topological Sort. It uses recursive topologicalSortUtil()
    def topologicalSort(self): 

        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological Sort starting from all vertices one by one
        for i in range(self.V): 
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Prints contents of stack
        print (" ",stack)

        # Prints contents of stack in reverse order
        print ("Following is a Reverse Topological Sort of the given graph:\n ",stack[::-1])

g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print ("Following is a Topological Sort of the given graph:")
g.topologicalSort()

