import heapq

def dijkstra(graph, start, end):
    # Initialize distances and previous nodes
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the end node, we're done
        if current_node == end:
            break
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we've found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct the path
    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return path, distances[end]

# Graph representation based on the image
# graph = {
#     'a': {'b': 2, 'c': 1, 'd': 4},
#     'b': {'a': 2, 'c': 2, 'e': 3},
#     'c': {'a': 1, 'b': 2, 'd': 2,'e': 5, 'f': 7},
#     'd': {'a': 4, 'c': 2, 'f': 4},
#     'e': {'b': 3, 'c': 5, 'g': 3},
#     'f': {'c': 7, 'd': 4, 'g': 1},
#     'g': {'e': 3, 'f': 1},
# }

graph = {
    'A': {'B': 1, 'E': 4, 'F': 8},
    'B': {'C': 2, 'F': 6, 'G': 6},
    'C': {'D': 1, 'G': 2},
    'D': {'G': 1, 'H': 4},
    'E': {'F': 5},
    'F': {},
    'G': {'F': 1, 'H': 1},
    'H': {},
}

# Find shortest path from 'a' to 'g'
# shortest_path, total_distance = dijkstra(graph, 'a', 'g')
shortest_path, total_distance = dijkstra(graph, 'A', 'H')

print(f"Shortest Path: {' -> '.join(shortest_path)}")
print(f"Total Distance: {total_distance}")