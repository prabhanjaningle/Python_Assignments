'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : Write a program which accept number from user and if number is less than 50 
//then print small , if it is greater than 50 and less than 100 then print medium, if it is 
//greater than 100 then print large.
//Date : 09-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def printNumber(Num):
    if Num < 50:
        print("Small")
    elif Num >= 50 and Num < 100:
        print("Medium")
    else:
        print("Large")

No1 = int(input("Enter your Number : "))
printNumber(No1)