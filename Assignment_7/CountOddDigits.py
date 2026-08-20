'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :  program which accept number from user and return the count of odd
//digits.
//Date : 11-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def CountOddDigits(Num):
    
        iCount = 0
        for i in range(1 , Num+1 , 1):
                if i % 2 != 0:
                        iCount += 1
        return iCount

No1 = int(input("Enter the number :- "))
No2 = CountOddDigits(No1)
print(No2)

    
