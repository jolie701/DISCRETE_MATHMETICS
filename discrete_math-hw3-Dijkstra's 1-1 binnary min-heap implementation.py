#-------------------------
#This code can run without a problem. 
#
#How to run: 
#1. Please input network filename: (例如輸入 input_100_400_1.sp)
#2. Then it does the shortest path calculation by Dijkstra's algorithm (min-heap)
#3. Then use a while loop to ask the user to input the origin (say, source)
#     if the origin is '0', then the code STOP
#     else the code will ask the user to input the destination, and output the shortest distance from s to t (i.e., Dst) and the entire path.
#
#This code is written by 張劭筠, email h34136091@gs.ncku.edu.tw, on 2026/5/31
#-------------------------
filename = input("Input your network filename = ")
From = []
To = []
L = []
OutDeg = []
OutEdge = []
n = 0

with open(filename, 'r') as file:
    for line in file:
        part = line.split()
        if part == []:
            continue #如果這行是空的則跳過空行 
        
        indicator = part[0]

        if indicator == 'p':
            n = int(part[2])
            # 節點編號通常從 1 到 n，所以我們開 n+1 大小
            OutDeg = [0] * (n + 1)
            for i in range(n + 1):
                OutEdge.append([])

        if indicator == 'a':
            tail = int(part[1])
            head = int(part[2])
            arc = float(part[3])

            From.append(tail)
            To.append(head)
            L.append(arc)
            
            # 因為這條邊是從 tail 指出去的，所以 tail 節點的出度 (OutDeg) 就要加 1
            OutDeg[tail] = OutDeg[tail] + 1 #原本是零，加一
            OutEdge[tail].append(len(From)-1)#先用 len(From) 算出這條邊在記帳本裡的編號是幾號
            #所以當for跑完，len(From)最後的數字就是邊數
            #OutDeg[source] 裡面存的是：這個節點「總共指出去幾條邊（邊數）」，不是長度!!!

def my_heappush(heap, item):
    """將 item (distance, node) 推進堆積，並向上調整 (Heapify Up)"""
    heap.append(item)
    curr = len(heap) - 1
    while curr > 0:
        parent = (curr - 1) // 2
        if heap[curr][0] < heap[parent][0]:
            heap[curr], heap[parent] = heap[parent], heap[curr]
            curr = parent
        else:
            break

#min heap
def my_heappop(heap):
    """彈出堆積頂端的最小值 (distance, node)，並向下調整 (Heapify Down)"""
    if not heap:
        return None
    if len(heap) == 1:
        return heap.pop()
    min_item = heap[0]
    heap[0] = heap.pop()
    curr = 0
    n_heap = len(heap)
    while True:
        left = 2 * curr + 1
        right = 2 * curr + 2
        smallest = curr
        if left < n_heap and heap[left][0] < heap[smallest][0]:
            smallest = left
        if right < n_heap and heap[right][0] < heap[smallest][0]:
            smallest = right
        if smallest != curr:
            heap[curr], heap[smallest] = heap[smallest], heap[curr]
            curr = smallest
        else:
            break
    return min_item

while True:
    source = int(input("Please input the source vertex index(0 to exit): "))
    if source == 0:
        print("程式結束")
        break
  
    destination = int(input("Please input the destination vertex index: "))
    
    #Dijkstra
    dist = [float('inf')]*(n + 1)
    parent = [None]*(n + 1)
    dist[source] = 0 #除了起點距離等於零，其他都設無限大
    min_heap = []
  
    my_heappush(min_heap, (0, source)) 
    
    while min_heap:
        pop_data = my_heappop(min_heap)
        if pop_data is None:
            break
        d, u = pop_data
      
        if u == destination:
            break
            
        if d > dist[u]:
            continue
            
        for edge_idx in OutEdge[u]:
            v = To[edge_idx]
            weight = L[edge_idx]
            
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                
                my_heappush(min_heap, (dist[v], v))
    
        # 3. 輸出結果
    if dist[destination] == float('inf'):
        print(f"從 {source} 到 {destination} 沒有可行路徑。")
    else:
        print(f"最短路徑長度 (Dst): {dist[destination]}")
        
        # 從終點逆向追蹤回起點
        path = []
        curr = destination
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
            
        path.reverse()  # 反轉回來變成 source -> ... -> destination
        print(f"整個路徑: {' -> '.join(map(str, path))}\n")
    
    
