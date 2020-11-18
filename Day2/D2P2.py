#day2 part 1
import os
def main():
    file = open("/Users/markmeade/Desktop/git/AOC2019/Day2/input.txt", "r")
    for line in file:
        array = line.split(',')
    intArray = []
    for item in array:
        intArray.append(int(item))
    initialArray = intArray[:]
    pos1 = 0
    pos2 = 0
    while intArray[0] != 19690720:
        intArray = initialArray[:]
        intArray[1] = pos1
        intArray[2] = pos2
        pos1+=1
        if pos1 == 99:
            pos1 = 0
            pos2 +=1
        if pos2 == 99:
            print("itterated through all posiblities.. no results")
        for index in range(0, len(intArray), 4):
                op = intArray[index]
                num1 = intArray[intArray[index + 1]]
                num2 = intArray[intArray[index + 2]]
                if op == 99:
                    break
                elif op == 1:
                    intArray[intArray[index+3]] = num1 + num2
                elif op == 2:
                    intArray[intArray[index+3]] = num1 * num2
        print('1 = ',pos1 ,'::: 2 = ', pos2 , "did not work")
    print ("position 1 = ",intArray[1], ' ... ',"position 2 = ",intArray[2])








main()