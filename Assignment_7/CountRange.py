'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :  program which accept number from user and return the count of digits in 
//between 3 and 7.
//Date : 11-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def CountRange(No1):
    iCount = 0
    for i in range(0,No1+1,1):
        if i >= 3 and i <= 7:
            iCount += 1 

    return iCount

Num1 = int(input("Enter the number :- "))
Num2 = CountRange(Num1)
print(Num2)