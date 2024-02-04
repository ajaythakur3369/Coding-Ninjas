'''
Task:- 
You are given a positive integer N. Return a list of integers of size 2N containing all the integers from 1 to N (both inclusive) twice arranged according to Langford pairing. If no such pairing exists return -1 is the only list element.

Note:
There may be more than one Langford pair possible, you need to return anyone permutation.

For example:
For N = 4, one possible Langford pairing will be:-
'''

'''
Constraints:- 
 1 <= T <= 5
 0 <= N <= 32
 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
2
4
5

Sample Output 1:
4 1 3 1 2 4 3 2 
-1
'''

'''
Sample Input 2:- 
1
15
Sample Output 2:
15 13 14 8 5 12 7 11 4 10 5 9 8 4 7 13 15 14 12 11 10 9 6 3 1 2 1 3 2 6
'''

from os import *
from sys import *
from collections import *
from math import *

def findLangford(n):
    if n % 4 == 1 or n % 4 == 2:
        ans = [-1]
        return ans
    ans = [0] * (2 * n)
    findLangfordHelper(ans, n)
    return ans
def findLangfordHelper(ans, n):
    if n == 0:
        return True
    for i in range(len(ans) - n - 1):
        if ans[i] == 0 and ans[i + n + 1] == 0:
            ans[i] = n
            ans[i + n + 1] = n
            if findLangfordHelper(ans, n - 1):
                return True
            ans[i] = 0
            ans[i + n + 1] = 0
    return False