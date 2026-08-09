'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : Accept single digit number from user and print it into word. 
//Date : 18-05-2025
////////////////////////////////////////////////////////////////////////////////////////////'''

def printDigitWord(Num):
    if Num == 1:
        print("One")
    elif Num == 2:
        print("Two")
    elif Num == 3:
        print("Three")
    elif Num == 4:
        print("Four")
    elif Num == 5:
        print("Five")
    elif Num == 6:
        print("Six")
    elif Num == 7:
        print("Seven")
    elif Num == 8:
        print("Eight")
    elif Num == 9:
        print("Nine")
    elif Num == 0:
        print("Zero")
    else:
        print("Invalid Input")

No1 = int(input("Entter your Number : "))
printDigitWord(No1)