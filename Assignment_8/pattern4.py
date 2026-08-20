'''////////////////////////////////////////////////////////////////////////////////////////////
//Author : Prabhanjan Sanjay Ingle
//Description : Print the Pattern from given input numbers
// 5
//# 1 * #  2 * # 3 * # 4 * # 5 *
//Date : 20-08-2026
////////////////////////////////////////////////////////////////////////////////////////////'''

def pattern(iNum):
    for i in range(1 , iNum+1):
        print('#' , end = " ")
        print(i , end = " ")
        print('*' , end = " ")

iNo = int(input("Enter the number :- "))
pattern(iNo)