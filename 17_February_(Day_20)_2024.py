'''
Task:- 
You are given two integer arrays ARR1 and ARR2 of length N and M respectively. You have to return true if ARR2 is a subset of ARR1, otherwise, return false.

For Example:
If the given arrays are [1, 2, 3] and [1, 2] then you need to return true as ARR2 is a subset of ARR1, but if the given arrays are [1, 2, 3] and [1, 2, 2] then you need to return false since ARR2 is not a subset of ARR1.
'''

'''
Constraints:- 
 1 <= T <= 10
 1 <= N <= 10^5
 0 <= ARR1[i] <= 10^9
 1 <= M <= 10^5
 0 <= ARR2[i] <= 10^9
 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
2
4
1 2 4 6
3
1 2 6
5
9 3 6 5
3
1 3 3

Sample Output 1:
true
false

Explanation For Sample Input 1:
For the first test case:
Here, all the elements of ARR2 are present in ARR1.
For the second test case:
All the elements of ARR2 are not present in ARR1, because there are two 3 in the ARR2 but only a single 3 in ARR1.
'''

'''
Sample Input 2:- 
2
3
2 3 4
2
4 3
4 
4 4 2 4
4
2 4 5 3

Sample Output 2:
true
false
'''

from os import *
from sys import *
from collections import *
from math import *

def checkSubset(arr1, arr2, n, m):
    
    '''
    Write your code here.  
    '''
    
    counts = {}
    for num in arr1:
        counts[num] = counts.get(num, 0) + 1


    '''
    Iterate through ARR2
    '''
    
    for num in arr2:
        
        '''
        If element not found or count is zero, return False
        '''
        
        if num not in counts or counts[num] == 0:
            return False
        
        '''
        Decrement the count of the element
        '''
        
        counts[num] -= 1

    return True