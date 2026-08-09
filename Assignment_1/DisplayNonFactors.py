'''//////////////////////////////////////////
// Program to Display Non factors....
/////////////////////////////////////////'''

def NonDisplayFactors(iNo):
    for i in range(1,iNo):
        if iNo % i != 0:
            print(i)
        

iNo1 = int(input("Enter the number to display nonfactors"))
NonDisplayFactors(iNo1)

