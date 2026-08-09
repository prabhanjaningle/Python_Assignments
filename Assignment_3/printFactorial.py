'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : Write a program to find factorial of given number. 
//Date : 09-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''
def printFact(No1):
    iMulti = 1
    if No1 == 0 or No1 == 1:
        iMulti = 1
        return iMulti
        
    else:
        for i in range(No1, 0 , -1):
            iMulti *= i
        return iMulti

No1 = int(input("Enter the number : "))
No2 = printFact(No1)
print(No2)
