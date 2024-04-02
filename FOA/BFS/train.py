# Graph Representation...

#           Member 1
#              |
# Singh--Member 2
#  |   \    |
#  |    \   |
#  |     \  |
# Member 3-Member 4
#  |        |
#  |        |
# Member 5  Member 6

#           Member 1
#              |
# Sharma--Member 2
#  |   \    |
#  |    \   |
#  |     \  |
# Member 3-Member 4
#  |        |
#  |        |
# Member 5

#           Member 1
#              |
# Rajput--Member 2
#  |     \
#  |      \
# Member 3

#           Member 1
#              |
# Mondal--Member 2
#  |   \    |
#  |    \   |
#  |     \  |
# Member 3-Member 4

#           Member 1
#              |
# Saptal--Member 2
#  |     \
#  |      \
# Member 3

#           Member 1
#              |
# Mishra--Member 2

#           Member 1
#              |
# Yadav--Member 1

#           Unknown


# graph = {
#     'Singh':['Member 1','Member 2','Member 3','Member 4','Member 5','Member 6'],
#     'Sharma':['Member 1','Member 2','Member 3','Member 4','Member 5'],
#     'Rajput':['Member 1','Member 2','Member 3'],
#     'Mondal':['Member 1','Member 2','Member 3','Member 4'],
#     'Saptal':['Member 1','Member 2','Member 3'],
#     'Mishra':['Member 1','Member 2'],
#     'Yadav':['Member 1'],
#     'Unknown':[]
# }

# visited = []
# queue = []


# def BFS(visited, graph, node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         current_node = queue.pop(0)
#         print(current_node, end='-->')

#         for neighbour in graph[current_node]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)


# print('BFS tree for the given graph is:')
# BFS(visited, graph, 'Member 1')



graph = {
    '1': ['3','7'],
    '3': ['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m , end=" ")

        for neighbor in graph [m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
bfs(visited,graph,'1')