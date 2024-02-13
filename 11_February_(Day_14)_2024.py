'''
Task:- 
The Champernowne constant C10 is defined by concatenating representations of successive integers: 12345678910111213....
Given an integer n, find the nth digit (1-based) of C10.
'''

'''
Constraints:- 
 5 <= N <= 200
'''

'''
Sample Input 1:- 
11

Sample Output 1:
0

Sample Output 1 Explanation:
11th digit of the C10 series is 0, 12345678910...., 11th digit is the 0 part of 10
'''

'''
Sample Input 2:- 
10

Sample Output 2:
1

Sample Output 2 Explanation: 
10th Digit of the C10 series is 1, 
12345678910 : here 1 is the 10th digit
'''

from math import *
from collections import *
from sys import *
from os import *

'''
Read input as specified in the question.
Print output as specified in the question.
'''

n=int(input())
k=""
for i in range(1,200):
    x=str(i)
    k+=x
    if len(k)>=n:
        print(k[n-1])
        break