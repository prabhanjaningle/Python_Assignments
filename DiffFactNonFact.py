'''/////////////////////////////////////////////////////
//Program to give difference between summation of
//factors and non-factors of given number
//////////////////////////////////////////////////'''

def DiffFactNonFact(iNo):
    iSum = 0
    iSum2 = 0
    iDiff = 0

    for i in range(1, iNo):
        if iNo % i == 0:
            iSum += i
        else:
            iSum2 += i
        
    iDiff = iSum2 - iSum
    return iDiff

iNumber = int(input("Enter the number to get their difference of factors and non factors"))
iNo2 = DiffFactNonFact(iNumber)

print(iNo2)

