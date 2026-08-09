'''///////////////////////////////////////////////////
// Program to take number and 
// print the odd numbers till that number
////////////////////////////////////////////////'''

def printOddNumbers(Num):
    for i in range(1 , Num , 1):
        if(i % 2 != 0):
            print(i)

No = int(input("Enter the number till you want your odd numbers are printed :- "))
printOddNumbers(No)