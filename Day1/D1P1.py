#aoc day 1
import math
def main():
    file = open("inputData.txt", "r")
    total = 0
    for line in file:
        while ((math.floor(int(line)/3)) - 2) > 0:
            num = math.floor(int(line)/3) - 2
            total += num
            line = num
    print(total)



main()