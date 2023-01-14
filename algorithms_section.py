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