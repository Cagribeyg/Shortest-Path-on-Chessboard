import numpy as np
from heapq import *
import itertools
import time
import sys
from random import randint
import math

#Sezgisel maliyet
def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

# A* algoritması Bilgisayar bilimlerinde en kısa yol bulmak için kullanılan algoritmalardan birisidir.
# Örneğin seyyar tüccar problemi (travelling salesman problem, TSP) gibi bir problemin çözümünde kullanılabilir. Benzer şekilde oyun programlamada, oyunda bulunan oyuncuların en kısa yolu bularak hedefe gitmeleri için de sıklıkla kullanılan algoritmadır.
# 3 farklı fonksiyon kullanılıyor. f(n) - sezgisel hesaplama. g(n) - toplam maliyet. h(n) toplam tahmin edilen maliyet
# Bu programda kullanılan algoritmanın mantığı ve implementasyonu Christian Careagadan esinlenmiştir
def astar(array, start, goal):
    #Robotun potansiyel olarak gidebileceği yerler, aşağı, yukarı, sağ, sol. Yani kısaca komşuları. Eğer robot çapraz gidebilseydi, aşağı kısıma (1,1),(1,-1),(-1,1),(-1,-1) da ekleyecektik.
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #İki set kullanmamız gerekiyor. Close set gittiğimiz yerleri hatırlamamızda yardımcı oluyor
    close_set = set()
    #Came from seti de bir önceki gittiğimiz kareyi tutuyor. Diğer bir deyişle parent ini tutuyor
    came_from = {}
    #Gerçek Maliyet
    g_puan = {start: 0}
    f_puan = {start: heuristic(start, goal)}
    #Heap structure nin define edilmesi. Heapler
    h_heap = []
    #İlk olarak başlangıç noktamızı heap e pushluyoruz
    heappush(h_heap, (f_puan[start], start))

    while h_heap:
        #Heapden popla
        current = heappop(h_heap)[1]

        if current == goal:
            data = []
            #Bulduğumuz data bi öncekinden gelmeyse
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        #Komşularını kontrol et
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tec_g_score = g_puan[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # Arrayin [i][j] j kısmını boundlar. Yani sütun kısmını
                    continue
            else:
                # Arrayin [i][j] i kısmını boundlar. Yani satır kısmını
                continue
            #Eğer bulduğumuz komşu close sette ise ve tentative g komşu g scoredan büyükse aramaya devam etsin
            if neighbor in close_set and tec_g_score >= g_puan.get(neighbor, 0):
                continue
            #Eğer deneme uzaklığımız asıl uzaklıktan küçük ise ve komşu eklediğimiz küme de değil ise
            if tec_g_score < g_puan.get(neighbor, 0) or neighbor not in [i[1] for i in h_heap]:
                came_from[neighbor] = current
                g_puan[neighbor] = tec_g_score
                f_puan[neighbor] = tec_g_score + heuristic(neighbor, goal)
                #Bulduğumuz ve koşullara uyan komşuyu heap e ekle
                heappush(h_heap, (f_puan[neighbor], neighbor))

    return False

# N x N lik matrix oluşturma fonksiyonu
def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]

#Engelleri rastgele koyma fonsiyonu
def calculateObstaclePlace(limit):
    return [randint(0, limit), randint(0, limit)]

def checkMatrix(adj_matrix, place):
    matrix_value = adj_matrix[place[0]][place[1]]
    return matrix_value == 0
#Board da koyma fonksiyonu
def placeInMatrix(adj_matrix, place):
    adj_matrix[place[0]][place[1]] = 1
    print("Rastgele engelin koyulduğu yer :", place)


# Matrix size'ı kullanıcıdan alma(Board size)
matrix_size = int(input("Lütfen matrix in boyutunu girin ( N x N) : "))

# Board oluşturma
adj_matrix = matrix(matrix_size, matrix_size, 0)
#Kenar sayısı
total_edge_count = int(math.pow(matrix_size, 2))

# Engel sayısını hesaplama
obstacle_count = int(total_edge_count / 10)
print("Engel sayısı:", matrix_size,"x",matrix_size,"/10","=", obstacle_count)

#Engelleri board a koyma
for j in range(obstacle_count):
    obstacle_place = calculateObstaclePlace(matrix_size - 1)
    if checkMatrix(adj_matrix, obstacle_place):
        placeInMatrix(adj_matrix, obstacle_place)

#Robotu rastgele noktaya koyma
i = 1
while (i > 0):
    # Rastgele sayı oluşturma
    rnd1 = randint(0, matrix_size - 1)
    rnd2 = randint(0, matrix_size - 1)
    # Robotu engel üstüne koymamamız için gerekli if statement
    if (adj_matrix[rnd1][rnd2] == 0):
        rbt_place1 = rnd1
        rbt_place2 = rnd2
        break
    else:
        i = i + 1



#Şimdi rastgele bir çıkış noktası belirliyoruz
i=1
while(i>0 ):
    #Rastgele sayı oluşturma
    rnd_exit1 = randint(0, matrix_size - 1)
    rnd_exit2 = randint(0, matrix_size - 1)
    # Çıkış noktası robotla ve engellerle aynı yerde olmamalı
    if(adj_matrix[rnd_exit1][rnd_exit2]== 0 and rnd_exit1 != rbt_place1 and rnd_exit2 != rbt_place2 ):
        exit_place1 = rnd_exit1
        exit_place2 = rnd_exit2
        break
    else:
        i=i+1
count_array_version=0
print("Status of board (Array gösterim versiyonu)")
for i in range(0,matrix_size):
    for j in range(0,matrix_size):
        print(i,j,"\t",end="")
        count_array_version=count_array_version+1
        if(count_array_version==matrix_size):
            print("\n")
            count_array_version=0
print("The status of Board (I lar gidilebilecek yol, O lar engel, R robot, E ise çıkış) :\n")
# Board un durumunu bastırma
count=0
for k in range(0,matrix_size):
    for j in range(0,matrix_size):
        if(adj_matrix[k][j]==0 ):
            #Robotun olduğu yeri bastırma
            if(k == rbt_place1 and j == rbt_place2):
                print("R\t",end="")
                count = count +1
                if(count == matrix_size):
                    print("\n")
                    count =0
            #Çıkışın olduğu yeri bastırma
            elif(k==exit_place1 and j == exit_place2):
                print("E\t", end="")
                count = count + 1
                if (count == matrix_size):
                    print("\n")
                    count = 0
            else:
                print("I\t", end="")
                count = count + 1
                if (count == matrix_size ):
                    print("\n")
                    count = 0
        #Engelleri bastırma
        elif (adj_matrix[k][j]==1):
            print("O\t", end="")
            count = count + 1
            if (count == matrix_size ):
                print("\n")
                count = 0
        else:
            print("Something went wrong")

print("Robotun bulunduğu konum: \n", rbt_place1, rbt_place2, )
print("Çıkış noktasının bulunduğu konum: \n",exit_place1,exit_place2,"\n\n")

#Elimizde robotun bulundugu koordinatlar ve çıkış noktasının bulundugu koordinatlar var
#Robotun koordinatları - rbt_place1, rbt_place2
#Çıkışın koordinatları - exit_place1, exit_place2

# A* algoritması numpy paketi içinde yapıldığı için, oluşturduğumuz arrayi numpy Arrayine çeviriyoruz
adj_nmpy = np.array(adj_matrix)

#Son olarak robotun ve çıkışın koordinatlarını, A* algoritmasının fonksiyonuna yazıyoruz
print("Gidilebilecek en kısa gidiş yolu")
print (astar(adj_nmpy, ( exit_place1,exit_place2), (rbt_place1,rbt_place2)),"(",exit_place1,exit_place2,")")
print("Board ın ilk elemanı 0,0 dir (En sol en üstteki element). Bir sağındaki eleman ise 0,1 olarak temsil edilmektedir. Bir altındaki eleman ise 1.0 olarak temsil edilmektedir")
print("Yani eğer sonuç 2,0  ,  2,1  , 3,1 diye çıkıyorsa, bu demektir ki önce sağa gitti sonra ise aşağıya gitti")
print("Olan pozisyonda ( örnek olarak 0,0) eğer sağa gidecekse sağa gittiği pozisyon 0,1 olur. Yani 0,0+1= 0,1")
print("Olan pozisyonda ( örnek olarak 0,0) eğer aşağı gidecekse aşağı gittiği pozisyon 1,0 olur. Yani 0+1,0= 1,0")
print("Olan pozisyonda (örnek olarak 1,0) eğer yukarı gidecekse yukarı gittiği pozisyon 0,0 olur. Yani 1-0,0 = 0,0 ")
print("Olan pozisyonda (örnek olarak 1,1) eğer sola gidecekse yukarı gittiği pozisyon 1,0 olur. Yani 1,1-1 = 1,0 ")

print("Belirtilen yollar soldan sağa array pozisyonu olarak gösterilmiştir. Yani robotun pozisyonundan çıkışın pozisyonuna soldan sağa gidiş şeklinde.")
