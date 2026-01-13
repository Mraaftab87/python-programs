# make calculator with functions

#arithmetic function
def arithmetic():
    e=input('Select the equation (/,*,+,-) : ')
    
    n1=int(input('Enter the 1 number : '))
    n2=int(input('Enter the 2 number : '))

    if e=='+':
        print('The addition is : ',n1+n2)
    elif e=='-':
        print('The subtraction is : ',n1-n2)
    elif e=='*':
        print('The multiplication is : ',n1*n2)
    elif e=='/':
        if n1==0 or n2==0:
            print("Invalid zero can't divided")
        else:
            print('Division is : ',n1/n2)
    else:
        print('Invalid input check again')
print('arithmetic sum')
arithmetic()