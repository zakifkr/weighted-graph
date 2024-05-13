import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))            
    return distances[end]

graf = {
    'Brebes' : {'Tegal': 50, 'Slawi': 30},
    'Tegal' : {'Brebes': 50, 'Slawi': 60, 'Pemalang': 40},
    'Slawi' : {'Brebes': 30, 'Tegal': 60, 'Purwokerto': 70},
    'Purwokerto' : {'Slawi': 70, 'Cilacap': 80, 'Kroya': 50, 'Kebumen': 60, 'Purbalingga': 40},
    'Pemalang' : {'Tegal': 40, 'Purbalingga': 90, 'Pekalongan': 30},
    'Purbalingga' : {'Purwokerto': 40, 'Pemalang': 90, 'Banjarnegara': 70},
    'Pekalongan' : {'Pemalang': 30, 'Kendal': 20},
    'Cilacap' : {'Purwokerto': 80, 'Kroya': 50},
    'Kroya' : {'Cilacap': 50, 'Purwokerto': 50, 'Kebumen': 40},
    'Kebumen' : {'Purwokerto': 60, 'Kroya': 40, 'Purworejo': 30}
}

start_node = input("Masukkan kota asal: ")
end_node = input("Masukkan kota tujuan: ")
distance = dijkstra(graph, start_node, end_node)
print("Jarak terpendek dari", start_node, "ke", end_node, "adalah", distance, "kilometer.")

