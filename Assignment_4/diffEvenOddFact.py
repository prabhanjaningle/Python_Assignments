'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :  program to find Difffernece Between Even and Odd factorial of given number. 
//Date : 09-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def difEvenOdd(No1):
    iMulti1 = 1
    iMulti2 = 1
    for i in range(1 , No1 + 1 , 1):
        if i % 2 == 0:
            iMulti1 *= i
        else:
            iMulti2 *= i
    if(iMulti1 > iMulti2):
        return iMulti1 - iMulti2
    else:
        return iMulti2 - iMulti1

no1 = int(input("Enter the number to get difference between even and odd factors : "))
No2 = difEvenOdd(no1)
print(No2)