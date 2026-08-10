'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :  program which accept number from user and display its digits in reverse order.
//Date : 10-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def ReverseDigit(No1):
    iTemp = 0
    iRev = 0
    iNo2 = No1
    while(iNo2 != 0):
        iTemp = iNo2 % 10
        iRev = iRev * 10 + iTemp
        iNo2 = iNo2//10
    return iRev

iNum = int(input("Enter the number to get its reversed :- "))
iNum2 = ReverseDigit(iNum)
print(f"Reverse of your number is :- {iNum2}")