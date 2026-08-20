'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : program which accept number from user and return multiplication of all 
//digits.
//Date : 20-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def multiply(n):
    iMulti = 1
    iTemp = 0
    iNo = n

    while(iNo != 0):
        iTemp = iNo % 10
        iMulti = iMulti * iTemp
        iNo //= 10

    return iMulti

n = int(input("Enter the number for the multiplication of digit :- "))
n2 = multiply(n)
print(n2)