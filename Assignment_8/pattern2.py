'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : Print the Pattern from given input numbers
// 5
// 5 # 4 # 3 # 2 # 1 #
//Date : 20-08-2025
////////////////////////////////////////////////////////////////////////////////////////////'''

def pattern2(n):
    for i in range(n , 0 , -1):
        print(i , end = " ")
        print('#' , end = " ")

iNum = int(input("Enter the number :- "))
pattern2(iNum)
