""" """ """ """ """ """ """ """ """ #Find the Runner-Up Score! 

if __name__=='__main__':
    n=int(input("son>"))
    arr=map(int, input("son kiriting").split())

print(sorted(set(arr),reverse=True)[0])
    


#Text Wrap
import textwrap

def wrap(string, max_width):
    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



#Python If-Else

import sys

N = int(input().strip())
if N % 2 != 0:
    print('Weird')
elif N >= 2 and N <= 5:
        print ("Not Weird")
elif N >= 6 and N <= 20:
        print ("Weird")
elif N > 20:
        print ("Not Weird")





#Write a function



def is_leap(year):
    leap = False
    
    if year % 400 ==0:
        return True
    if year % 100 ==0:
        return False
    if year % 4 ==0:
        return True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))







#input()

x,k=map(int, input().split())
p = input()
print(k==eval(p))


#Set .add() 

N = int(input())

countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))


#Integers Come In All Sizes


a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(a**b+c**d)




#Capitalize

import os

def solve(s):
    for i in s.split():
        s=s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close() 

#Zipped!


N=map(int,input("SON").split())
X=map((float,input("BALL").split()) for i in range(N[1]))
for i in zip(*X):
    print(sum(i)/N[1]) 





 #Any or All

N=int(input('nechta>'))

boxs=[]

for i in range(N):
    boxs.append(input('qiymat bering>'))
    if bool(boxs)==True:
        print('True')
    else:
        print('False') 

#2xil usl

n = int(input())
numbers = list(map(int,input().split()))
count = 0
count_palindrome = 0
for element in numbers:
    if element > 0:
        count += 1
for i in range(len(numbers)):
    string = str(numbers[i])
    counts = 0
    for j in range(len(string)//2):
        if string[j] == string[-1-j]:
            counts += 1
    if counts == len(string)//2:
        count_palindrome += 1
if count_palindrome > 0 and count ==len(numbers):
    print(True) 



#DefaultDict Tutorial



from collections import defaultdict

n, m = map(int,input('').split())

a = defaultdict(list)
for i in range(1, n + 1):
    a[input('')].append(i)

for i in range(1, m + 1):
    key = input('')
    if len(a[key]) > 0:
        print(" ".join(str(c) for c in a[key]))
    else:
        print(-1) 

#Power - Mod Power

a=int(input('enter a>'))
b=int(input('enter b>'))
m=int(input('enter m>'))
print(pow(a,b))
print((a**b)%m)


#Set .union() Operation


n=input()
n1=set(map(int,input().split()))
b=input()
b1=set(map(int,input().split()))

x=n1.union(b1)
print(len(x)) 



#Check Subset

T = int(input())

for _ in range(T):
    a = input()
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))

"""

#Polar Coordinates


from cmath import sqrt,phase
c = complex(input())

print(sqrt(pow(c.real,2)+pow(c.imag,2)).real)
print(phase(complex(c.real,c.imag))) 





#Array


import numpy

def arrays(arr):
    
    # complete this function
    # use numpy.array
    return numpy.array(arr[:: -1],float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)



#Set .intersection() Operation

first_num = int(input())
first_set = set(map(int, input().split()))
second_num = int(input())
second_set = set(map(int, input().split()))
print (len(first_set.intersection(second_set)))




#Set .difference() Operation


first_name=int(input())
first_set=set(map(int,input().split()))
second_name=int(input())
second_set=set(map(int,input().split()))
print(len(first_set.difference(second_set)))