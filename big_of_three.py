n1=int(input('Enter the 1 number: '))
n2=int(input('Enter the 2 number: '))
n3=int(input('Enter the 3 number: '))

if n1>=n2 and n1>n3:
    print('first is biggest')
elif n2>=n3 and n2>n1:
    print('second is biggest')
else:
    print('Third is biggest')