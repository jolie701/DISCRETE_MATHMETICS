#-------------------------
#This code can run without problem.
#
#How to run: 
#(!!詳細解釋運行此程式的步驟!! 例如像下面這樣寫:)
#1. input the network filename  
#2. it reads the file and stores the graph by adjacency matrix and list  
#3. it asks the user to input a source node index s, and a data structure type, and then print out adjacent arcs (s,j).
#4. it repeats step 3, unless s=0, which terminates the code 
#
#This code is written by 張劭筠, email H34136091@gs.ncku.edu.tw, on 2026/05/16
#-------------------------

filename = input("Input your network filename = ")
#把your filename得到的答案輸入進filename
n = 0
m = 0
tail = 0
head = 0
arc = 0 

#if A[1][5] = 1,C[1][5] = 12,代表1跟5之間有連通(1)，且長度為12
From = []
To = []
L = []


with open(filename, 'r') as file:
    for line in file:
        part = line.split()
        if part == []:
            continue #如果這行是空的則跳過空行 
        
        indicator = part[0]

        if indicator == 'p':
            n = int(part[2]) #part[2]拿到的會是"100"，屬於文字
            m = int(part[3])
            A = []
            C = []
            OutEdge = []
            OutDeg = [0] * (n + 1)
        
        #可以創AC的矩陣空間，用迴圈寫一維，再用.append()疊起來
            for i in range(n + 1):
             # 直接把長度為 n + 1 的零陣列塞進大箱子
                A.append([0] * (n + 1))
                C.append([0] * (n + 1))
                OutEdge.append([]) # 裡面是一個個空的小 list

        if indicator == 'a':
            tail = int(part[1])
            head = int(part[2])
            arc = float(part[3])
            A[tail][head] = 1
            C[tail][head] = arc

            From.append(tail)
            To.append(head)
            L.append(arc)
            
            # 因為這條邊是從 tail 指出去的，所以 tail 節點的出度 (OutDeg) 就要加 1
            OutDeg[tail] = OutDeg[tail] + 1 #原本是零，加一
            OutEdge[tail].append(len(From)-1)#先用 len(From) 算出這條邊在記帳本裡的編號是幾號
            #所以當for跑完，len(From)最後的數字就是邊數
            #OutDeg[source] 裡面存的是：這個節點「總共指出去幾條邊（邊數）」，不是長度!!!

       
while True:
    source = int(input("Please input the source vertex index(0 to exit): "))
    if source == 0:
        print("程式結束")
        break
    choice = input("Please choose (1) Adjacency Matrix (2) Adjacency List: ")

    if choice == '1':
        print(f"\n--- 透過【鄰接矩陣】查詢節點 {source} ---")
        found_out = False
        #怎麼用矩陣找邊
        for j in range(1, len(A)):
            if A[source][j] == 1:
                print(f"該指出邊 ({source} -> {j})，長度為: {C[source][j]}")
                found_out = True
        if found_out == False:
            print("  （此節點沒有任何指出邊）")
        
        found_in = False
        print("")
        for i in range(1, len(A)):
            if A[i][source] == 1:
                print(f"該指入邊 ({i} -> {source})，長度為: {C[i][source]}")
                found_in = True
        if found_in == False:
            print("  （此節點沒有任何指入邊）")

    elif choice == '2':
        found_out = False
        print(f"\n--- 透過【鄰接串列】查詢節點 {source} ---")
        #怎麼用串列找邊
        for k in range(len(From)): #k會從0開始跑
            if From [k] == source:#檢查第k條邊，它的出發點是不是source
                print(f"該指出邊 ({source} -> {To[k]})，長度為: {L[k]}")
                found_out = True
        if found_out == False:  
            print("  （此節點沒有任何指出邊）")

        found_in = False
        print("")
        for l in range(len(From)):
            if To[l] == source:#檢查第l條邊，看它的終點是不是source
                print (f"該指入邊 ({From[l]} -> {source})，長度為: {L[l]}")
                found_in = True
        if found_in == False:
            print("  （此節點沒有任何指入邊）")
    else:
        print("輸入錯誤，請輸入 1 或 2！")