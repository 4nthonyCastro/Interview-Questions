# =========================
# [Title] - Depth-first search (DFS) Algorithm for tree traversal on graph
# =========================
# [DFS Function Description, Lines 32 to 37]: 
#             1. Starts by checking if the current node is unvisited 
#                -> If current node is visited, it's marked by appending the node to the visited set.
#
#             2. DFS function is invoked for each neighbor node of the current node
#                -> Occurs only when current node visited is True. 
#
#             3. The base case is invoked when all nodes are marked as visited
#                -> The Function then returns 
# ========================
# [Notes]:
#             Average Time Complexity of O(1),
#                -> This is due o the fact that all nodes and vertices are visited 
#                -> This average time complexity only applies to Trees
#                -> Using a list would result in a higher complexity
# [INCOMPLETE WORK, 01/06/20]
# =========================

# Dictionary named myTask
myTask = {
    'A' : ['B'],
    'B' : ['A'],
    'C' : ['D', 'E'],
    'D' : [],
    'E' : ['G']
}

# Tracks already visited nodes
visited = set() 

def dfs(visited, myTask, node):
    if node not in visited: 
        print (node)
        visited.add(node)
        for neighbourNode in myTask[node]:
            dfs(visited, myTask, neighbourNode)

# Driver
dfs(visited, myTask, 'A')
