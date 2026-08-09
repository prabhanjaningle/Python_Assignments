'''///////////////////////////////////////////////////
// Program to take number and 
// print the number Line of Number
////////////////////////////////////////////////'''

def printNumberLine(Num):
    for i in range(-Num , Num+1 , 1):
        print(i, end = " ")
    

Num1 = int(input("Enter the number that you want numberLine of"))
printNumberLine(Num1)