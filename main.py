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
