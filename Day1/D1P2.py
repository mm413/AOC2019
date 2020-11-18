#aoc day 2
import math
import os
def main():
    file = open("/Users/markmeade/Desktop/git/AOC2019/Day1/inputData.txt", "r")
    total = 0
    for line in file:
        while ((math.floor(int(line)/3)) - 2) > 0:
            num = math.floor(int(line)/3) - 2
            total += num
            line = num
    print(total)



main()