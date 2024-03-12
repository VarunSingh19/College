from collections import deque

def bfs(start_plane):
    visited = set()
    queue = deque([start_plane])

    while queue:
        current_plane = queue.popleft()
        if current_plane not in visited:
            print("Moving to plane", current_plane)
            visited.add(current_plane)

            # Perform actions like fighting terrorists and saving passengers here

            for neighbor in get_neighbors(current_plane):
                if neighbor not in visited:
                    queue.append(neighbor)

def get_neighbors(plane):
    # Define the connections between planes based on the scenario
    connections = {
        1: [2],
        2: [1, 3, 4],
        3: [2],
        4: [2, 5],
        5: [4, 6],
        6: [5, 7],
        7: [6]
    }
    return connections.get(plane, [])

# Start the BFS from plane 1
bfs(1)