'''///////////////////////////////////////
//Program to Diplay Factors in Reverse 
//order....
///////////////////////////////////'''

def DisplayRevFactors(iNo):
    for i in range(iNo - 1 , 0 , -1):
        if iNo % i == 0:
            print(i)


iNo = int(input("Enter the number to display the factors in reverse : "))
DisplayRevFactors(iNo)