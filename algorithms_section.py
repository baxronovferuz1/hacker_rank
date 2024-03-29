#Solve Me First


def solveMeFirst(a,b):
    return a+b
	# Hint: Type return a+b below


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


#Plus Minus


import math
import os
import random
import re
import sys



N=int(input())
number=input().split()

result={"positive":0, "negative":0,"zero":0}
for i in number:
    if int(i)>0:
        result["positive"]+=1
    elif int(i)<0:
        result["negative"]+=1
    else:
        result["zero"]+=1
        
        
        
print(format(result["positive"]/N))
print(format(result["negative"]/N))
print(format(result["zero"]/N))


#Mini-Max Sum

import math
import os
import random
import re
import sys

a = sorted(map(int,input().split()))
print(sum(a[:4]),sum(a[1:]))


#Staircase


import math
import os
import random
import re
import sys


n=int(input())
m=" "
t=1
while n>n-n:
    print((n-1)*m+t*("#"))
    n=n-1
    t=t+1



#A Very Big Sum

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#Birthday Cake Candles

N=int(input())
candles=list(map(int,input().split()))
print(candles.count(max(candles)))



#Beautiful Days at the Movies

import math
import os
import random
import re
import sys



def beautifulDays(i, j, k):
    count=int(0)
    for i in range(i,j+1):
        if (i-int(str(i)[::-1]))%k==0:
            count+=1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()




#Cats and a Mouse


import sys


q = int(input().strip())
for i in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    if abs(x - z) < abs(y - z):
        print('Cat A')
    elif abs(x - z) > abs(y - z):
        print('Cat B')
    else:
        print('Mouse C')


#Compare the Triplets



    
import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    pointa=0
    pointb=0
    ar = []
    for i in range(3):
        if a[i]>b[i]:
            pointa+=1
            
        if a[i]<b[i]:
            pointb+=1
    ar.insert(0,pointa)
    ar.insert(1,pointb)        
    return(ar)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


#Find Digits


import math
import os
import random
import re
import sys



def findDigits(n):
    num_divisor = 0
    num_digit = math.floor(math.log10(n))+1
    for i in range(num_digit):
      d = (n//10**i) % 10
      if ((d != 0) and (n % d == 0)):
         num_divisor = num_divisor + 1
    return num_divisor
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
 


#Sales by Match

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    pair = 0
    d = {}
    for i in ar:
        if i in d:
            d[i] += 1
        if i not in d:
            d[i] = 1
    print(d)
    for x in d:
        u = d[x]//2
        pair += u
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
