'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : Print the Pattern from given input numbers
// 5
// A B C D E
//Date : 20-08-2025
////////////////////////////////////////////////////////////////////////////////////////////'''

def Pattern(iNo):
    ch = 'A'
    for i in range(0 , iNo):
        print(ch , end = " ")
        ch = chr(ord(ch) + 1)


iNum = int(input("Enter the number"))
Pattern(iNum)