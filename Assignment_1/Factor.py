'''////////////////////////////////////
//Program to find multiplication
//of factors of given number
////////////////////////////////////'''

def FindFactor(iFact):
    no = 1 
    iMul = 1
    for i in range(iFact-1):
        if iFact % no == 0:
            iMul *= no
        
        no += 1 

    return iMul

iNo = int(input("Enter the number you wanted to find multiplication of factors : "))



iNo2 = FindFactor(iNo)
print(iNo2)
