# Define a graph using an adjacency list representation

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : [],
  '8' : []
}

# Set to keep track of visited node during DFS traversal
visited = set()
# Depth-First Search (DFS) function to traverse the graph
def dfs(visited,graph,node):
    # Check if the current node has been visited.
    if node not in visited:
        # Print the current node, separated by a space 
        print(node , end=" ")
        # mark the current node as visited.
        visited.add(node)
        # Recursively explore neighbors of the current node.
        for neighbors in graph[node]:
            dfs(visited,graph,neighbors)
# Display the result of DFS traversal starting from node '5'
print("Name: Varun Singh\nClass: SYBSC CS\nRoll no: 999")
print("The following is the tree traversal using DFS: ")
dfs(visited,graph,'5')