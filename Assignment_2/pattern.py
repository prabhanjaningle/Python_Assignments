'''///////////////////////////////////////
//Print the pattern taking input from user
//Input : 5
//output : $ * $ * $ * $ * $ *
///////////////////////////////////////
'''

def pattern1(no1):
    for i in range(1 , no1):
        print("$ * ", end = " ")


no1 = int(input("Enter the number for pattern"))
pattern1(no1)

