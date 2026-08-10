'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :  program to find Odd factorial of given number. 
//Date : 09-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def getOddFactor(No1):
    iMul = 1
    for i in range(1 , No1 + 1, 1):
        if i % 2 != 0:
            iMul *= i
        
    return iMul

No1 = int(input("Enter the number to get the odd factorial : "))
No2 = getOddFactor(No1)
print(No2)


