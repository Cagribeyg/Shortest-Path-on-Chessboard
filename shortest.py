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
rbttemp1=rbt_place1
rbttemp2=rbt_place2
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
    def __init__(self, data1,data2):
        self.data1 = data1
        self.data2=data2
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


root_robot = Node(rbt_place1,rbt_place2)




#Finding robot neirbrough
countOfneirbough = 0

#For up
# if(adj_matrix[rbt_place1-1][rbt_place2]==1 and rbt_place1-1 >=0 ):
#     countOfneirbough= countOfneirbough+1
#     p = Node(rbt_place1-1,rbt_place2)
#     root_robot.add_child(p)
#     print("Up founded")
#
# #For down
# if(rbt_place1+1 ==matrix_size):
#     print("Fault for down")
# else:
#     if(adj_matrix[rbt_place1+1][rbt_place2]==1   ):
#         if(rbt_place1+1 ==matrix_size):
#             print("Fault for down")
#         else:
#             countOfneirbough = countOfneirbough + 1
#             q = Node(rbt_place1 + 1, rbt_place2)
#             root_robot.add_child(q)
#             print("Down founded")
#
# #For right
# if(rbt_place2+1 == matrix_size):
#     print("fault for right")
# else:
#     if(adj_matrix[rbt_place1][rbt_place2+1]==1  ):
#         if(rbt_place2+1 == matrix_size):
#             print("fault for right")
#         else:
#             countOfneirbough = countOfneirbough+1
#             r = Node(rbt_place1 , rbt_place2+1)
#             root_robot.add_child(r)
#             print("Right founded")
#
# #For left
# if(adj_matrix[rbt_place1][rbt_place2-1]==1 ):
#     if( rbt_place2-1 < 0):
#         print("fault for left")
#     else:
#         countOfneirbough = countOfneirbough + 1
#         print("Left founded")
#         s = Node(rbt_place1 , rbt_place2- 1)
#         root_robot.add_child(s)


print("Count of adjacency",countOfneirbough)

#Initial neigbour of the robot, they were be added as children
for c in root_robot.children:
    print("Neighbour :",c.data1, c.data2)

clr = matrix(matrix_size, matrix_size, "WHITE")


def traverse(seekpoint1,seekpoint2):
    if(seekpoint1==exit_place1 and seekpoint2==exit_place2):
        return "seek point 1, seek point 2", seekpoint1,seekpoint2
    else:
        # For up
        if (adj_matrix[seekpoint1 - 1][seekpoint2] == 1 and clr[seekpoint1 - 1][
            seekpoint2] == "WHITE" and seekpoint1 - 1 >= 0):
            print("Up recursion found,", seekpoint1 - 1, seekpoint2)
            clr[seekpoint1 - 1][seekpoint2] = "BLACK"
            seekpoint1 = seekpoint1 - 1
            seekpoint2 = rbt_place2
            p = Node(seekpoint1, seekpoint2)
            root_robot.add_child(p)
            traverse(seekpoint1, seekpoint2)
        #For Down
        if(rbt_place1+1==matrix_size):
            print("fault in recursion down")
        else:
            if (adj_matrix[rbttemp1 + 1][rbttemp2] == 1 and clr[rbttemp1+1][rbttemp2]=="WHITE" and rbttemp1+1 !=matrix_size ):
                clr[rbttemp1+1][rbttemp2]="BLACK"
                print("Down recursion found,",rbttemp1+1,rbttemp2)
                seekpoint1=rbttemp1+1
                seekpoint2=rbttemp2
                q = Node(seekpoint1,seekpoint2)
                root_robot.add_child(q)
                traverse(seekpoint1,seekpoint2)
        #For right
        if(rbttemp2==matrix_size):
            print("Fault for right recursion")
        else:
            if (adj_matrix[rbttemp1][rbttemp2 + 1] == 1 and clr[rbttemp1][rbttemp2+1]=="WHITE" and rbttemp2+1 != matrix_size):
                clr[rbttemp1 ][rbttemp2+ 1] = "BLACK"
                print("Right recursion found,", rbttemp1 , rbttemp2+ 1)
                seekpoint1 = rbttemp1
                seekpoint2 = rbttemp2 + 1
                r = Node(seekpoint1, seekpoint2)
                root_robot.add_child(r)
                traverse(seekpoint1, seekpoint2)
        #For left
        if (adj_matrix[rbttemp1][rbttemp2 - 1] == 1):
            if (rbttemp2 - 1 < 0):
                print("Fault for left recursion")
            elif(rbttemp2 - 1 > 0 and clr[rbttemp1][rbttemp2-1]=="WHITE"):
                print("Left recursion found,", rbttemp1, rbttemp2 - 1)
                clr[rbttemp1 ][rbttemp2-1] = "BLACK"
                seekpoint1 = rbttemp1 -1
                seekpoint2 = rbttemp2
                s = Node(seekpoint1, seekpoint2)
                root_robot.add_child(s)
                traverse(seekpoint1, seekpoint2)


traverse(rbt_place1,rbt_place2)
print("Traversedan çıktı")
for i in root_robot.children:
    print("asd")



