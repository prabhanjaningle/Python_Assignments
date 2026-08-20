'''///////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :   program which accept number from user and return difference between 
//summation of even digits and summation of odd digits. 
//Date : 20-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def DifEvenOdd(No1):

    iEvenSum = 0
    iOddSum = 0
    iTemp = 0
    iNo = No1
    while(iNo != 0):
        iTemp = iNo % 10
        if iTemp % 2 == 0:
            iEvenSum += iTemp
        else:
            iOddSum += iTemp

        iNo //= 10

    return iEvenSum - iOddSum

Num1 = int(input("Enter the number :- "))
Num2 = DifEvenOdd(Num1)
print(Num2)