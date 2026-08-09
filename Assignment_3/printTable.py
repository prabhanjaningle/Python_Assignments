'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : Write a program which accept number from user and display its table.  
//Date : 19-05-2025
////////////////////////////////////////////////////////////////////////////////////////////'''

def printTable(No1):
    for i in range(1 , 11 , 1):
        print(f"{No1} * {i} = {No1 * i}")

Num = int(input("Enter the number to get the table : "))
printTable(Num)