'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :  program to find even factorial of given number. 
//Date : 09-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def getEvenFactorial(no1):
    iMul = 1
    for i in range(1 , no1+1 , 1):
        if(i % 2 == 0):
            iMul *= i
        
    return iMul

No1 = int(input("Enter the number to get the even factorial : "))
No2 = getEvenFactorial(No1)
print(No2)