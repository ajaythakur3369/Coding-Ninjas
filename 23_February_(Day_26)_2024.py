'''
Task:- 
This time we are executing a program containing ‘N’ functions on a single-threaded CPU. Each function has a unique ‘ID’ between 0 and (N-1) and each time it starts or ends, we write a log with the ID, whether it started or ended, and the TIMESTAMP.

You are given a 2D array of integers containing information about ‘L’ logs where ith column represents the ith log message. Each column contains 3 rows to describe the ith log where,

1st Row - represents the ID of the function.
2nd Row - represents whether the function has started or ended where 1 denotes the start and -1 denotes the end.
3rd Row - represents the TIMESTAMP of the log.

You are required to return an array where the value at the ith index represents the exclusive time for the function with ID ‘i’.

For Example:
Consider the following input
0 1 1 1 2 2 1 0
1 1 1 -1 1 -1 -1 -1
0 2 5 7 8 10 11 14

Thus, we return [5, 7, 3] as a process with ID 0 has taken 5 units of time and process with ID 1 has taken 7 units of time and process ID 2 has taken 3 units of time. A process’s exclusive time is the sum of exclusive times for all function calls in the program. As process Id 1 has called itself so exclusive time is the sum of exclusive times(5 + 2).
'''

'''
Constraints:- 
 1 <= T <= 10
 1 <= N <= 10 ^ 2
 2 <= L <= 5 * (10 ^ 2) and L is even.
 0 <= TIMESTAMP <= 10 ^ 9
 Time Limit: 1 sec.
'''

'''
Sample Input 1:- 
1
2 4
0 1 1 0
1 1 -1 -1
0 2 5 6

Sample Output 1:
3 4

Explanation for Input 1:
Function 0 starts at the beginning of timestamp 0, then it executes for 2 units of time and reaches the end of timestamp 1. 

Function 1 starts at the beginning of timestamp 2, executes for 4 units of time, and ends at the end of timestamp 5. 

Function 0 resumes execution at the beginning of timestamp 6 and executes for 1 unit of time.  

So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
'''

'''
Sample Input 2:- 
1
1 6
0 0 0 0 0 0
1 1 -1 1 -1 -1
0 2 5 6 6 7
Sample Output 2:
8
'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def exclusiveTime(logs, n, l):
    
    '''
    Write your Code here.
    '''
    
    stk = []
    ans = [0] * n

    for i in range(l):
        if logs[1][i]==-1:
            x = stk[-1][1]
            t = logs[2][i] - x + 1
            ans[logs[0][i]] += t
            stk.pop()
            if stk:
                stk[-1] = (stk[-1][0], logs[2][i] + 1)
        else:
            if stk:
                ans[stk[-1][0]] += logs[2][i] - stk[-1][1]
            stk.append((logs[0][i], logs[2][i]))

    return ans

'''
Main Code.
'''

t = int(input().strip())

for i in range(t):
    n,l = list(map(int, stdin.readline().strip().split(" ")))
    logs = []
    id = list(map(int, stdin.readline().strip().split(" ")))
    start_end = list(map(int, stdin.readline().strip().split(" ")))
    timestamp = list(map(int, stdin.readline().strip().split(" ")))
    logs.append(id)
    logs.append(start_end)
    logs.append(timestamp)

    ans = exclusiveTime(logs, n, l)

    for ele in ans:
        print(ele, end =" ")

    print()



