#day2 part 1
import os
def main():
    file = open("/Users/markmeade/Desktop/git/AOC2019/Day2/input.txt", "r")
    for line in file:
        array = line.split(',')
    intArray = []
    for item in array:
        intArray.append(int(item))
    for index in range(0, len(intArray), 4):
            op = intArray[index]
            num1 = intArray[intArray[index + 1]]
            num2 = intArray[intArray[index + 2]]
            if op == 99:
                print("the answer is: ", intArray[0])
                break
            elif op == 1:
                intArray[intArray[index+3]] = num1 + num2
            elif op == 2:
                intArray[intArray[index+3]] = num1 * num2








main()