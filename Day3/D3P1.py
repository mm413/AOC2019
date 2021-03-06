#day 3 part 1
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
    for direction in line1:
        # print(direction[0])
        if direction[0] == 'U':
            direction = direction[1:]
            for i in range(int(direction)):
                curx+=1
                matrix[cury][curx] = 1
        elif direction[0] == 'D':
            direction = direction[1:]
            for i in range(int(direction)):
                curx-=1
                matrix[cury][curx] = 1
        elif direction[0] == 'R':
            direction = direction[1:]
            for i in range(int(direction)):
                cury+=1
                matrix[cury][curx] = 1
        elif direction[0] == 'L':
            direction = direction[1:]
            for i in range(int(direction)):
                cury-=1
                matrix[cury][curx] = 1
# put wire 2 on grid
    curx = mid
    cury = mid
    for direction in line2:
        if direction[0] == 'U':
            direction = direction[1:]
            for i in range(int(direction)):
                curx+=1
                if matrix[cury][curx] == 0:
                    matrix[cury][curx] = 2
                else:
                    matrix[cury][curx] = '+'
        elif direction[0] == 'D':
            direction = direction[1:]
            for i in range(int(direction)):
                curx-=1
                if matrix[cury][curx] == 0:
                    matrix[cury][curx] = 2
                else:
                    matrix[cury][curx] = '+'
        elif direction[0] == 'R':
            direction = direction[1:]
            for i in range(int(direction)):
                cury+=1
                if matrix[cury][curx] == 0:
                    matrix[cury][curx] = 2
                else:
                    matrix[cury][curx] = '+'
        elif direction[0] == 'L':
            direction = direction[1:]
            for i in range(int(direction)):
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

    for line in matrix:
        print(line)

def build2dArray(x):
    return [[0 for i in range(x)] for j in range(x)]

main()