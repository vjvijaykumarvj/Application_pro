'''# the enumurate function used to convert the data collective object to enumurate objects'''
'''
# enumurate 
x = ['hello ', 'welcome', 'to', 'python']
for i,j in enumerate(x):
    print(i,j)
'''

'''from functools import reduce
l = range(11)
print(reduce(lambda x,y:x+y,l))
'''

'''# Write the reverse the numbers
l = str(input('Enter number'))
m = (l[::-1])
if l == m:
    print(l)
else:
    print(m)'''

'''
# Print the arm strong Number Using Python
n = int(input('Enter number'))
a = map(int,str(n))
b = map(lambda x:x**3,a)
if sum(b)==n:
    print('Arm Strong')
else:
    print('Not')
'''

'''#2nd largest number using python
l = [10, 1, 20, 11, 30, 90, 40, 50]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]<l[j]:
            l[i],l[j] = l[j],l[i]
print(l)
'''

'''l = ['1', '0', '-1', '10', '-10']
m = [int(i) for i in l]
m.sort()
print(m)'''

'''a = [1,11,2,34,32,5,88,7]
list = []
for i in a:
    if i>10:
        list.append(i)
print(list)'''

'''
Print the common letters using python
s = 'madhubala'
s1 = 'hariharan'
m = set(s) & set(s1)
for i in m:
    print(i)
'''

# find the factorial numbers using python
'''
l = 5
factirial = 1
if l>1:
    for i in range(1,1+l):
        factirial=factirial*i
print(factirial)
'''

'''
# Print the calender
import calendar
year = int(input('Enter year'))
month = int(input('Enter month'))
for month in range(1,1+month):
    print(calendar.month(year,month))
'''

'''
l = [100,200,20,40,212,67,87,789,90,0,9,1000]
def FindingNumbers(l,N):
    l.sort()
    print(l[-N:])
N = 3
FindingNumbers(l,N)
'''

'''
# print the repeated numbers
s = 'hello guru namaskaram'
m = {i:s.count(i) for i in s}
print(m)
'''

'''
import string
m = 'hello guru namaskaram'
print(string.capwords(m))
print(m.title())
print(m.find('s'))
'''

'''
m = {'A':10, 'B':20, 'C':30, 'D':40, 'E':50}
s = {j:i for i,j in m.items()}
print(s)
'''

'''
s = [10,2,5,4,6,8,78,78,10,34,54,12]
m = list({i for i in s if s.count(i)>1})
print(m)

l = []
for i in (set(s)):
    if s.count(i)>1:
        l.append(i)
print(l)

'''

'''
d = {'A':10, 'B':20, 'C':30, 'D':40, 'E':50}
m = ['A', 'D']
print({i:d[i] for i in m})


for i in m:
    if d.pop(i):
        print(d)
'''

'''
l = ['M', 'NA', 'I', 'VIJ']
l1 = ['Y', 'ME', 'S', 'AY']
s = [i+j for i,j in zip(l,l1)]
print(s)
'''

'''
l = ['Hello ', 'Dear ']
l1 = ['Sir', 'Take']
m = [i+j for i in l for j in l1]
print(m)
'''

'''
l = [10,20,30]
l1 = [100,200,300]
for i,j in zip(l,l1[::-1]):
    print(i,j)
'''

'''
l = [10, 20, 30, 20, 40, 50, 20]
m = []
for i in l:
    if i!=20:
        m.append(i)
print(m)
'''

'''
n = int(input('Enter number'))
n1 = int(input('Enter number'))

for i in range(n,n1+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)
'''

'''
n = int(input('Enter number'))

for i in range(2,n):
    if n%i==0:
        print(n,'Not Prime')
        break
else:
    print(n,'Prime')
'''

'''
n = ['malli', 23, 267.5, 'sai', 56.5, 'kumar', 678]
name = []
number = []
decimal = []
for i in n:
    if type(i) == int:
        number.append(i)
    if type(i) == str:
        name.append(i)
    if type(i) == float:
        decimal.append(i)
print(name)
print(number)
print(decimal)
'''

'''
s = 'hello/23/@b$8$012.,!'
num = []
name = []
extra = []
for i in s:
    if i.isdigit():
        num.append(i)
    elif i.isalpha():
        name.append(i)
    else:
        extra.append(i)
print(' '.join(num))
print(' '.join(name))
print(' '.join(extra))
'''
"""
username = 'vijay'
password = 12345

c_username = (input('Enter Username'))
c_password = int(input('Enter Password'))

if username == c_username and password == c_password:
    print(
        '''
        1. Deposite
        2. Withdraw
        3. Mini Statement
        4. Exit
        '''
    )
    amount = 55000
    option = int(input('Enter option'))
    if option == 1:
        dep = int(input('Enter Amount'))
        amount += dep
        print('Total Amount',amount)
    elif option == 2:
        withdraw = int(input('Enter Amount'))
        amount -= withdraw
        print('TotalAmount',amount)
    elif option == 3:
        print('!!!!!! Hello Welcome ATM !!!!!!!')
        print('Welcome ',username)
        print('Total Amount',amount)
        print('Thanks for visit')
    elif option == 4:
        print('Exit')
    else:
        print('Please Enter valid User and Password')
"""

'''
# Anagram find using Python

def is_anagram(s,s1):
    return set(s) == set(s1)
print(is_anagram('evil','live'))
'''



# file handling

# use of file handling read the data from file or write the data to the file



# the exceptions are raised when the syntically progreme is correct but its lead to error the error does not stop excection of code
# then we use the exception

# try block used to when the test the block of the code errors
# except block used to the the handling the errors
# else block used to there is no exceptions its excecute
# finally block used to its will excecute any time




