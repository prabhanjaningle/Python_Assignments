'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : program which accept number from user and count frequency of such a 
                digits which are less than 6. 
//Date : 10-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def CountFourFreq(iNo):
    iTemp = 0
    iNo2 = iNo
    iCount = 0
    while(iNo2 != 0):
        iTemp = iNo2 % 10
        if iTemp < 6:
            iCount += 1
        iNo2//=10
    return iCount

Num = int(input("Enter the number to get frequency of digits less than 6 :- "))
Num2 = CountFourFreq(Num)
print(Num2)

