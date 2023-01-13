#Find the Runner-Up Score! 

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




#Set .symmetric_difference() Operation

first_num = int(input())
first_set = set(map(int, input().split()))

second_num = int(input())
second_set = set(map(int, input().split()))

print(len(first_set.symmetric_difference(second_set)))



#Mod Divmod

a=int(input())
b=int(input())
print(a//b)
print(a%b)
print(divmod(a,b))



#itertools.permutations()

from itertools import permutations

S = input().split()

for i in sorted(permutations(S[0], int(S[1]))):
    print(''.join(i))



#Introduction to Sets

def average(array):
    # your code goes here
    return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)



#Symmetric Difference

M=int(input())
Mset=set(map(int,input().split()))
N=int(input())
Nset=set(map(int,input().split()))


Mdiff=Mset.difference(Nset)
Ndiff=Nset.difference(Mset)

result=Mdiff.union(Ndiff)

for i in sorted(list(result)):
    print(i)



#Exceptions

x = int(input())
for i in range(x):
    try:
        a, b = input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as v:
        print("Error Code:",v)




#Set .discard(), .remove() & .pop()

n = input()
s = set(map(int, input().split())) 
a = int(input())

for i in range(a):
    k = []
    k = input().split()
    if k[0] == 'pop':
        s.pop()
    elif k[0] == 'remove':
        s.remove(int(k[1]))
    elif k[0] == 'discard':
        s.discard(int(k[1]))
    else:
        print('not a command')
print(sum(s))


#Check Strict Superset

A = set(map(int, input().split()))
for i in range(int(input())):
    X = set(map(int, input().split()))
    if A.issuperset(X) != True or len(A) == len(X): 
        print(False)
        break 
else: print(True)
        


#Collections.deque()


from collections import deque
d = deque()
for i in range(int(input())):
    k =input().split()
    if k[0] == 'append':
        d.append(int(k[1]))
    elif k[0] == 'pop':
        d.pop()
    elif k[0] == 'popleft':
        d.popleft()
    elif k[0] == 'appendleft':
        d.appendleft(int(k[1]))
print(' '.join(map(str,d)))



#Concatenate

import numpy
P, N, M = map(int,input().split())
A = numpy.array([input().split() for _ in range(P)],int)
B = numpy.array([input().split() for _ in range(N)],int)
print(numpy.concatenate((A, B), axis = 0))




#itertools.combinations()

from itertools import combinations

s, k = input().split()
k = int(k)
s = sorted(s)
for i in range(1, k+1):
    for c in list(combinations(s, i)):
        print(''.join(c))


#Min and Max

import numpy





n,m=map(int,input().split())

lista=[list(map(int,input().split())) for i in range(n)]

ar=numpy.array(lista)

print(max(numpy.min(ar,axis=1))) 



#Floor, Ceil and Rint

import numpy as np


np.set_printoptions(legacy='1.13')

A = np.array(list(map(float,input().split())))

print(np.floor(A))

print(np.ceil(A))

print(np.rint(A))



#Dot and Cross

import numpy

N = int(input())
A = numpy.array([input().split() for i in range(N)], int)
B = numpy.array([input().split() for i in range(N)], int)
print(numpy.dot(A, B))




#Concatenate


import numpy

P, N, M = map(int,input().split())

A = numpy.array([input().split() for i in range(P)],int)
B = numpy.array([input().split() for i in range(N)],int)

print(numpy.concatenate((A, B), axis = 0))




#Python Evaluation

#from __future__ import print_function
eval(input())

#Map and Lambda Function

cube = lambda x:x**3
 # complete the lambda function 

def fibonacci(n):
    ls = [0, 1]
    for i in range(2,n):
        ls.append(ls[i-1] + ls[i-2])
    return ls[:n]
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())

    print(list(map(cube, fibonacci(n))))




#Re.split()

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re

print("\n".join(re.split(regex_pattern, input())))


#itertools.product()


from itertools import product

A = input().split()
A = list(map(int,A))
B = input().split()
B = list(map(int, B))

output = list(product(A,B))

for i in output:
    print(i, end = " ");


# collections.Counter()

from collections import Counter

x = int(input())
sizes = list(map(int,input().split()))

n = int(input())
sizes = Counter(sizes)
pr = 0
for i in range(n):
    sz,pz = map(int,input().split())
    if(sizes[sz]):
        sizes[sz] -= 1
        pr += pz
print(pr)



#Introduction to Sets

def average(array):
    return sum(set(arr))/len(set(arr))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)




#Collections.namedtuple()

N, headers, total = int(input()), list(input().split()), 0
for _ in range(N):
    total += int(list(input().split())[headers.index('MARKS')])
print(total/N)



#Detect Floating Point Number


for i in range(int(input())):
    n=input()
    try:
        if n.isdigit():
            print("False")
        else:
            float(n)
            print("True")
    except:
        print("False")
    