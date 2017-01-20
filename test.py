import itertools
import time
import sys
from random import randint
import math

def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]

def colorr(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]

def calculateObstaclePlace(limit):
    return [randint(0, limit), randint(0, limit)]

def checkMatrix(adj_matrix, place):
    matrix_value = adj_matrix[place[0]][place[1]]
    return matrix_value == 1

def placeInMatrix(adj_matrix, place):
    adj_matrix[place[0]][place[1]] = 0
    print("obstacle placed in :", place)

# get the size of the matrix
matrix_size = int(input("Enter a number: "))
loop_size = matrix_size
# construct adjacency matrix
adj_matrix = matrix(matrix_size, matrix_size, 1)
print(adj_matrix)

# calculate total edge count
total_edge_count = int(math.pow(matrix_size, 2))
print("total edge count: ", total_edge_count)

# calculate obstacle count
obstacle_count = int(total_edge_count / 10)
print("obstacle_count:", obstacle_count)

#TODO check if obstacle place is save (else case)
for j in range(obstacle_count):
    obstacle_place = calculateObstaclePlace(matrix_size - 1)
    if checkMatrix(adj_matrix, obstacle_place):
        placeInMatrix(adj_matrix, obstacle_place)

print(adj_matrix)

#Now place the robot in random place
i=1
while(i>0 ):
    rnd1 = randint(0, matrix_size - 1)
    rnd2 = randint(0, matrix_size - 1)
    #Robot should not be located at obstacle
    if(adj_matrix[rnd1][rnd2]== 1):
        rbt_place1 = rnd1
        rbt_place2 = rnd2
        strr= "X position of robot is:" , rnd1, "Y position of robot is:" , rnd2
        break
    else:
        i=i+1
print("Robot placed in: \n",rbt_place1,rbt_place2,"\n\n")

print("The status of Board :\n")
# Now printing the area
count=0
for k in range(0,matrix_size):
    for j in range(0,matrix_size):
        if(adj_matrix[k][j]==1 ):
            if(k == rbt_place1 and j == rbt_place2):
                print("R\t",end="")
                count = count +1
                if(count == loop_size):
                    print("\n")
                    count =0
            else:
                print("X\t", end="")
                count = count + 1
                if (count == loop_size ):
                    print("\n")
                    count = 0

        elif (adj_matrix[k][j]==0):
            print("O\t", end="")
            count = count + 1
            if (count == loop_size ):
                print("\n")
                count = 0
        else:
            print("Something went wrong")

# Now calculate a random exit point
i=1
while(i>0 ):
    rnd_exit1 = randint(0, matrix_size - 1)
    rnd_exit2 = randint(0, matrix_size - 1)
    # Exit place should not be same as robot place and should not be located in obstacle
    if(adj_matrix[rnd_exit1][rnd_exit2]== 1 and rnd_exit1 != rbt_place1 and rnd_exit2 != rbt_place2 ):
        exit_place1 = rnd_exit1
        exit_place2 = rnd_exit2
        break
    else:
        i=i+1
print("Exit placed in: \n",exit_place1,exit_place2,"\n\n")

#Implementing tree and nodes
class Node(object):
    def __init__(self, data1,data2,parent1,parent2):
        self.data1 = data1
        self.data2=data2
        self.parent1=parent1
        self.parent2=parent2
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)



root_robot = Node(rbt_place1,rbt_place2,0,0)


#Initialize all the points as NOT ADDED
clr = matrix(matrix_size, matrix_size, "NOT ADDED")
clr[rbt_place1][rbt_place2]="ADDED"



def final_traverse(position1,position2):
    #Check conditions
    up = 0
    down = 0
    right = 0
    left = 0



    #First mark robot place as Added
    clr[position1][position2] = "ADDED"
    #For up neighbour
    if(adj_matrix[position1-1][position2]==1 and position1-1>=0 and clr[position1-1][position2]!="ADDED"):

        clr[position1-1][position2] = "ADDED"
        p= Node(position1-1,position2,position1,position2)

        print("Up neighbour is added:",position1-1,position2)
        up=1

    #For down neighbour
    if(position1+1==matrix_size):
        print("")
    else:
        if(adj_matrix[position1+1][position2]==1 and position1+1!=matrix_size and clr[position1+1][position2]!="ADDED"):

            clr[position1+1][position2 ] = "ADDED"
            q = Node(position1 + 1, position2, position1, position2)
            print("Down neighbour is added:", position1 + 1, position2)
            down=1

    #For right neighbour
    if(position2+1==matrix_size):
        print()
    else:
        if(clr[position1][position2+1] == "ADDED"):
            print()
        else:
            if(adj_matrix[position1][position2+1]==1 and position2+1 !=matrix_size and clr[position1][position2+1 != "ADDED"]):
                r = Node(position1 , position2+1, position1, position2)
                clr[position1][position2+1]="ADDED"
                print("Right neighbour is added:", position1 , position2+1)
                right=1

    #For left neighbour
    if(position2-1<0):
        print()
    else:
        if(adj_matrix[position1][position2-1]==1 and position2-1>=0 and clr[position1][position2-1] != "ADDED"):

            clr[position1][position2 -1] = "ADDED"
            s = Node(position1, position2 - 1, position1, position2)
            print("Left neighbour is added:", position1 , position2- 1)
            left=1








final_traverse(rbt_place1,rbt_place2)

shortest_count=0
for i in root_robot.children:
    print("Values are: ",i.data1, i.data2, "Parent is",i.parent1,i.parent2)


print("\n")
print("Exit placed in:",exit_place1,exit_place2)
print("Robot placed in:",rbt_place1,rbt_place2)

print("-------------------------------------------------------------------\n")

def findingParent1(point1,point2):
    for j in root_robot.children:
        if(j.data1==point1 and j.data2==point2):
            return j.parent1
def findingParent2(point1,point2):
    for j in root_robot.children:
        if(j.data1==point1 and j.data2==point2):
            return j.parent2
current_position1=exit_place1
current_position2=exit_place2

p=1

# while(p>0):
#     #Finding parent of current
#     temp_parent1 = findingParent1(current_position1, current_position2)
#     temp_parent2 = findingParent2(current_position1, current_position2)
#     #Creating a node
#     t1 = Node(current_position1,current_position2,temp_parent1,temp_parent2)
#     print("T1 are",t1.data1,t1.data2,"\t",t1.parent1,t1.parent2)
#     current_position1 = temp_parent1
#     current_position2 = temp_parent2
#     newprt1 = findingParent1(current_position1,current_position2)
#     newprt2 = findingParent2(current_position1, current_position2)
#
#     newNode = Node(temp_parent1,temp_parent2,newprt1,newprt2)
#     print("New node are", newNode.data1,newNode.data2,"\t",newNode.parent1,newNode.parent2)
#
#     if(newNode.data1==rbt_place1 and newNode.data2==rbt_place2):
#         break
#     else:
#         shortest_count=shortest_count+1
#
# print("Shortest",shortest_count+1)