# //////////////////////////////////////
# // Program to Sum All the non factors
# //////////////////////////////////////

def SumNonFactors(iNo):
    iSum = 0
    for i in range(1, iNo):
        if iNo % i != 0:
            iSum += i
    
    return iSum

iNo = int(input("Enter the number to calculate sum of its non factors : "))
iNo2 = SumNonFactors(iNo)
print(iNo2)