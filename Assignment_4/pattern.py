'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : program which accept number from user and display below pattern.
//order.
//No = 4
 * # * # * # * #
//Date : 09-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def printPattern(No1):
    for i in range(0 , No1 , 1):
        print("*" , end = " ")
        print("#" , end = " ")
    
no1 = int(input("Enter the number to print pattern : "))
printPattern(no1)