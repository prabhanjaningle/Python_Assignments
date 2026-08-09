'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : Write a program which accept number from user and display its table in reverse 
//order.
//Date : 09-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def iRevTable(No):
    for i in range(10 , 0 , -1):
        print(f"{No} * {i} = {No * i}")
    
Num = int(input("Enter the number to get reverse table : "))
iRevTable(Num)