#Baris ini mengimpor modul heapq dari Python. Modul ini menyediakan implementasi dari algoritma heap, yang digunakan dalam algoritma Dijkstra untuk mengatur simpul dalam antrian berdasarkan jarak terpendek.
import heapq

# Fungsi dijkstra didefinisikan dengan tiga parameter: graph yang merupakan representasi dari graf, start yang merupakan simpul awal, dan end yang merupakan simpul tujuan.
def dijkstra(graph, start, end):
    #Membuat dictionary distances untuk menyimpan jarak terpendek dari simpul awal ke setiap simpul lainnya. Awalnya, semua jarak diatur ke infiniti (float('inf')), kecuali jarak dari simpul awal ke dirinya sendiri yang diatur ke 0.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    #Membuat antrian prioritas queue yang berisi pasangan (jarak, simpul). Awalnya, antrian ini hanya berisi simpul awal dengan jarak 0.
    queue = [(0, start)]
    
    # Selama antrian tidak kosong, mengambil simpul dengan jarak terpendek dari antrian menggunakan fungsi heappop dan menyimpan jarak dan simpul tersebut ke dalam current_distance dan current_node.
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        #Jika simpul saat ini adalah simpul tujuan, maka algoritma berhenti.
        if current_node == end:
            break
        
        #Jika jarak saat ini lebih besar dari jarak terpendek yang sudah diketahui ke simpul saat ini, maka simpul ini diabaikan.
        if current_distance > distances[current_node]:
            continue
        
        #Untuk setiap tetangga dari simpul saat ini, menghitung jarak baru ke tetangga tersebut. Jika jarak baru ini lebih pendek dari jarak terpendek yang sudah diketahui ke tetangga tersebut, maka jarak terpendek ke tetangga tersebut diperbarui dan tetangga tersebut ditambahkan ke antrian dengan jarak baru tersebut.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
            

    return distances[end]

# Contoh graf berbobot yang merepresentasikan keterhubungan antar kota di Jawa Tengah.
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


