'''///////////////////////////////////////////////////
// Program to take number and 
// print the numbers till that number arrives
////////////////////////////////////////////////'''

def printNumbers(Num):
    for i in range(0,Num):
        print(i , end = " ")


Num = int(input("Enter the number till you wanted to print"))
printNumbers(Num)


