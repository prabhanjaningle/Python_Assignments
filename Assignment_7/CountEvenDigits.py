'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :  program which accept number from user and return the count of even 
//digits.
//Date : 11-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def CountEvenDigits(No1):
    iCount = 0
    for i in range(0,No1+1,1):
        if i % 2 == 0:
            iCount += 1
    return iCount

Num = int(input("Enter the number :- "))
Num2 = CountEvenDigits(Num)
print(Num2)
