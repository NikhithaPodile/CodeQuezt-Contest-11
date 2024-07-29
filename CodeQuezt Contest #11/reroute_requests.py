from collections import deque, defaultdict

def reroute_requests(n, connections, events):
    # Initialize the adjacency list for the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize server status
    alive = [True] * n

    # Function to find the smallest alive server using BFS
    def find_smallest_alive(start):
        if alive[start]:
            return start
        visited = [False] * n
        queue = deque([start])
        smallest_alive = float('inf')
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if alive[neighbor]:
                    smallest_alive = min(smallest_alive, neighbor)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return smallest_alive if smallest_alive != float('inf') else -1

    results = []
    for event in events:
        event_type, server = event
        if event_type == 1:  # request
            result = find_smallest_alive(server)
            results.append(result)
        elif event_type == 2:  # failure
            alive[server] = False

    return results

# Sample Input
n = 6
connections = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5]
]
events = [
    [1, 0],
    [1, 1],
    [2, 2],
    [1, 2],
    [1, 3],
    [2, 4],
    [1, 4],
    [1, 5]
]

# Expected Output: [0, 1, 0, 3, 0, 5]

# Calling the function with the sample input
output = reroute_requests(n, connections, events)
print(output)
