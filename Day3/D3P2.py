#day 3 part 2
import os
import math
def main():
    file = open("/Users/markmeade/Desktop/git/AOC2019/Day3/inputTest.txt", "r")
    # file = open("/Users/markmeade/Desktop/git/AOC2019/Day3/input.txt", "r")
    size = 9
    matrix = build2dArray(size)
    #when accessing matrix, [y][x]
    mid = math.floor(size/2)
    matrix[mid][mid] = 'X'
    count =0
    for line in file:
        if count == 1:
            line2 = line.rstrip().split(',')
        else:
            line1 = line.rstrip().split(',')
            count =1
    print('line1: ',line1)
    print('line2: ',line2)


    # put wire 1 on grid
    curx = mid
    cury = mid
    # print(line1)
    line1moves = 0
    line2moves = 0
    for direction in line1:
        # print(direction[0])
        if direction[0] == 'U':
            direction = direction[1:]
            for i in range(int(direction)):
                line1moves+=1
                curx+=1
                matrix[cury][curx] = 1
        elif direction[0] == 'D':
            direction = direction[1:]
            for i in range(int(direction)):
                line1moves+=1
                curx-=1
                matrix[cury][curx] = 1
        elif direction[0] == 'R':
            direction = direction[1:]
            for i in range(int(direction)):
                line1moves+=1
                cury+=1
                matrix[cury][curx] = 1
        elif direction[0] == 'L':
            direction = direction[1:]
            for i in range(int(direction)):
                line1moves+=1
                cury-=1
                matrix[cury][curx] = 1
# put wire 2 on grid
    curx = mid
    cury = mid
    for direction in line2:
        if direction[0] == 'U':
            direction = direction[1:]
            for i in range(int(direction)):
                line2moves+=1
                curx+=1
                if matrix[cury][curx] == 0:
                    matrix[cury][curx] = 2
                else:
                    matrix[cury][curx] = '+'
        elif direction[0] == 'D':
            direction = direction[1:]
            for i in range(int(direction)):
                line2moves+=1
                curx-=1
                if matrix[cury][curx] == 0:
                    matrix[cury][curx] = 2
                else:
                    matrix[cury][curx] = '+'
        elif direction[0] == 'R':
            direction = direction[1:]
            for i in range(int(direction)):
                line2moves+=1
                cury+=1
                if matrix[cury][curx] == 0:
                    matrix[cury][curx] = 2
                else:
                    matrix[cury][curx] = '+'
        elif direction[0] == 'L':
            direction = direction[1:]
            for i in range(int(direction)):
                line2moves+=1
                cury-=1
                if matrix[cury][curx] == 0:
                    matrix[cury][curx] = 2
                else:
                    matrix[cury][curx] = '+'
    points = []
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == "+":
                points.append([i,j])
    manhat = 100000
    for myset in points:
        distance1 = abs(mid - myset[0])
        distance2 = abs(mid - myset[1])
        tempManhat = distance2 + distance1
        if tempManhat < manhat:
            xy = (distance1, distance2)
            manhat = tempManhat
    print(manhat, xy)

    # for line in matrix:
    #     print(line)

    #now I need to trace the wires.
    # trace wire 1 by following all of the 1's out of X. count for every 1.
    # When you hit a '+', follow 2's out until you hit X (go first direcion, and opposite)
    # take the smaller of the two numbers, and add it to a list.



    curr1 = mid
    curr2 = mid
    oneCounter = 0
    twoCounter = 0
    while True:
        if matrix[curr1][curr2] == '+':
            if matrix[curr1][curr2 + 1] == 2:
                # at an intersection and 2 to the right
            if matrix[curr1][curr2 -1] == 1:
                # at an intersection and 2 to the left
            if matrix[curr1 + 1][curr2] == 1:
                # at an intersection and 2 to the above
            if matrix[curr1 - 1][curr2] == 1:
                # at an intersection and 2 directly belowx


        if matrix[curr1][curr2 + 1] == 1:
            # 1 to the right
            curr2+=1
        if matrix[curr1][curr2 -1] == 1:
            # 1 to the left
           curr2-=1
        if matrix[curr1 + 1][curr2] == 1:
            #  1 above
            curr1+=1
        if matrix[curr1 - 1][curr2] == 1:
            # 1 below
            curr1-=1



    def build2dArray(x):
        return [[0 for i in range(x)] for j in range(x)]
main()