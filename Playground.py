from os import system
import time
# Time Clock(start)
start = time.time()

# print('# program to print statement')
print('WELCOME TO PROGRAMMING IN PYTHON')
print()

# print('# program to find the total mark of three subjects')
m1=int(input('ENTER MARK_1: '))
m2=int(input('ENTER MARK_2: '))
m3=int(input('ENTER MARK_3: '))
sum=m1+m2+m3
print('\nTHE TOTAL MARK: ',sum)
print()

# print('# program to find area of a circle')
r=int(input('ENTER THE RADIUS: '))
a=3.14*r*r
print('\nAREA OF CIRCLE = ',a)
print()

# print('# program to print character with respect to input ascii value')
ch=int(input('ENTER AN ASCII CODE: '))
print('\nEQUIVALENT CHARACTER OF',ch,'IS',chr(ch))
print()

# print('# program to find curved surface area of a cylinder')
r=float(input('ENTER THE RADIUS(in cms): '))
h=float(input('ENTER THE HEIGHT(in cms): '))
csa=(2*3.14*r)*h
#system('cls')
system('clear')
print('RADIUS:',r,'cms')
print('HEIGHT:',h,'cms')
print('\nCURVED SURFACE AREA OF CYLINDER IS',csa,'sq.cms')
print()

# print('# program to illustrate dynamic intialization')
num1=int(input('ENTER NUMBER_1: '))
num2=int(input('ENTER NUMBER_2: '))
sum=int(num1+num2)
print('\nAVERAGE:',sum/2)
print()

# print('# program to find perimeter and area of a semi-circle')
radius=int(input('ENTER RADIUS(in cms): '))
pi=float(3.14)
perimeter=float((pi+2)*radius)
area=float((pi*radius*radius)/2)
print('\nPERIMETER OF SEMICIRCLE IS',perimeter,'cms')
print('AREA OF SEMICIRCLE IS',area,'cms')
print()

# print('# program to declare referance variable')
num=int(100)
temp=num
print('\nVALUE OF NUM',num)
print('VALUE OF TEMP',temp)
print()

# print('# program to calculate net salary')
basic=float(input('ENTER THE BASIC SALARY:....'))
da=float(input('ENTER THE DEARNESS ALLOWANCE:....'))
hra=float(input('ENTER THE HOUSE RENT ALLOWNCE:....'))
gross=float(basic+da+hra)
gpf=float((basic+da)*0.10)
tax=float(gross*0.10)
np=gross-(gpf-tax)
print()
print('                         BASIC PAY : ','                   ',basic)
print('                         DEAR ALLOWANCE : ','              ',da)
print('                         HOUSE RENT ALLOWANCE : ','        ',hra)
print('                         GROSS PAY : ','                   ',gross)
print('                         G.P.F : ','                       ',gpf)
print('                         INCOME TAX : ','                  ',tax)
print('                         NET PAY : ','                     ',np)
print()

# print('# explicit conversion problems')
varf=178.25255685
print(float(varf))
print(int(varf))
print()

# print('# program to check whether a person is eligible to vote using if statement')
age=int(input('ENTER YOUR AGE: '))
if age>=18:
    print('\nYOUR ARE ELIGIBLE FOR VOTING....')
print('THIS STATEMENT IS ALWAYS EXECUTED.')
print()

# print('# program to find whether the given number is even number or odd number using if-else statement')
num=int(input('ENTER A NUMBER: '))
rem=num%2
if rem==0:
    print('\nTHE GIVEN NUMBER',num,'IS EVEN')
else:
    print('\nTHE GIVEN NUMBER',num,'IS ODD')
print()

# print('# program to calculate commission according to grade using nested if statement')
sales=int(input('ENTER SALES AMOUNT: '))
grade=(input('ENTER GRADE: '))
if sales>5000:
    commission=sales*0.10
    print('\nCOMMISSION:',commission)
else:
    commission=sales*0.05
    print('\nCOMMISSION:',commission)
print('GOOD JOB....')
print()

# print('# program to find the greatest of two numbers using conditional operator')
a,b=int(input('ENTER ANY TWO NUMBERS: ')),int(input())
largest=a if a>b else b
print('LARGEST NUMBER:',largest)
print()

# print('# program to demonstrate switch(if-elif-else) statement')
num=int(input('ENTER WEEK DAY NUMBER: '))
if num==1:
    print('\nSUNDAY')
elif num==2:
    print('\nMONDAY')
elif num==3:
    print('\nTUESDAY')
elif num==4:
    print('\nWEDNESDAY')
elif num==5:
    print('\nTHURSDAY')
elif num==6:
    print('\nFRIDAY')
elif num==7:
    print('\nSATURDAY')
else:
    print('\nWRONG INPUT')
print()

# Time Clock(end)
end = time.time()
# Time elapsed(start-end)
seconds = end - start

# Print time executed
print('Execution time: {0:.03f} s'.format(seconds))
