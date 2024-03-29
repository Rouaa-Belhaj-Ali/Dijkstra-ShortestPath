from collections import deque

def dijkstra(graph, start):
    queue = deque([start])
    dist = {start: 0}
    while queue:
        current = queue.popleft()
        for neighbor, weight in graph[current].items():
            new_dist = dist[current] + weight
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                queue.append(neighbor)
    return dist

graph = {'A': {'B': 135, 'C': 4}, 'B': {'E': 5}, 'C': {'E': 161, 'D': 2}, 'D': {'E': 3}, 'E': {}}
distance = dijkstra(graph, 'A')
print("Distances:", distance)
