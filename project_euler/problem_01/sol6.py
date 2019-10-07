'''
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
'''
from __future__ import print_function
try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3
 
'''store  multiples of 3 and 5 in a set and then add''' 
n = int(input().strip())
l = set()
x = 3
y = 5
while(x<n):
    l.add(x)
    x+=3
while(y<n):
    l.add(y)
    y+=5
print(sum(l))
