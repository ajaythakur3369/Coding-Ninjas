'''
Task:- 
Given a square binary matrix ‘mat[n][n]’, find ‘K’ such that all elements in the Kth row are ‘0’ and all elements in the Kth column are ‘1’. The value of mat[k][k] can be anything (either ‘0’ or ‘1’). If no such k exists, return ‘-1’.

For example:
Consider the following matrix :
0 1 1 
0 1 0 
1 1 0 

You can see that row 1 (0-based) contains all 0’s except mat[1][1] and column 1 contains all 1’s. Hence the answer for the above case is 1.
'''

'''
Constraints:- 
 1 <= T <= 5
 1 <= N <= 1000
 0 <= Aij <= 1
 Time Limit: 1sec
'''

'''
Sample Input 1:- 
1
3
0 1 1 
0 1 0 
1 1 0 

Sample Output 1:
1

Explanation For Sample Output 1:
For the first test case, column 1 contains all ones. Also except mat[1][1] all numbers in row 1 are 0.
'''

'''
Sample Input 2:- 
2
2
0 1
1 0
2
0 0
1 0

Sample Output 2:
-1
0
'''

from os import *
from sys import *
from collections import *
from math import *

def findRowK(mat):
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat)):
            if i != j and mat[i][j] == 0 and mat[j][i] == 1:
                count += 1
        if count >= (len(mat) - 1):
            return i
    return -1
