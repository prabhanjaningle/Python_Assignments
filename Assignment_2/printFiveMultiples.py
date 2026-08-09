'''///////////////////////////////////////////////////
// Program to take number and 
// print the First 5 multiples of it
////////////////////////////////////////////////'''

def printFiveMultiples(No1):
    for i in range(1 , 6 , 1):
        print(No1 * i)

Num = int(input("Enter the number you wanted the five multiples of"))
printFiveMultiples(Num)
