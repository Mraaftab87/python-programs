s1=int(input('Enter the marks of subject 1: '))
s2=int(input('Enter the marks of subject 2: '))
s3=int(input('Enter the marks of subject 3: '))

subject=[s1,s2,s3]

tot_marks=s1+s2+s3
percentage=tot_marks/len(subject)

print('total marks is: ',tot_marks)
print('percentage is: ',percentage)

if percentage>=40:
    print('Pass')
else:
    print('Fail')