""" """ """ """ #Find the Runner-Up Score! 

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