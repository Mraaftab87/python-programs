s1=int(input('Enter the marks of subject 1: '))
s2=int(input('Enter the marks of subject 2: '))
s3=int(input('Enter the marks of subject 3: '))
s4=int(input('Enter the marks of subject 4: '))
s5=int(input('Enter the marks of subject 5: '))
s6=int(input('Enter the marks of subject 6: '))
s7=int(input('Enter the marks of subject 7: '))

subject=[s1,s2,s3,s4,s5,s6,s7]

tot_marks=s1+s2+s3+s4+s5+s6+s7
pr=tot_marks/len(subject)

print('total marks is: ',tot_marks)
print('percentage is: ',pr)

if pr<33:
    print('F')
elif pr>=90:
    print('A+')
elif pr>=80:
    print('A')
elif pr>=70:
    print('B')
elif pr>=60:
    print('C')
elif pr>=50:
    print('D')
elif pr<=33:
    print('E')
else:
    print('Invalid')