'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description :  program which accept number from user and check whether it contains 0 
                 in it or not.
//Date : 10-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def isContainZero(iNo):
     bCheck = False
     iNo2 = iNo
     iTemp = 0
     while(iNo2 != 0):
          iTemp = iNo2 % 10
          if iTemp == 0:
               bCheck = True
               break
          iNo2 = iNo2//10
     return bCheck

No1 = int(input("Enter the number to check it contains zero or not :- "))
bChecker = isContainZero(No1)
if bChecker == True:
     print("It contains zero")
else:
     print("It does not contain a zero")