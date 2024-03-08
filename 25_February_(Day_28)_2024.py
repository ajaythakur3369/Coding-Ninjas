'''
Task:- 
You are given an array ‘sum’ which is the prefix sum of an array of coins ‘C’ where ‘C[i]’ is ‘1’ if the coin is real, or ‘0’ if the coin is fake. There is exactly one fake coin in the array.
Return the index of the fake coin. Assume the array to be 0-indexed.

For Example:
‘sum’ = {1,1,2,3} 
Index of the fake coin is 1. 
For the given ‘sum’, ‘C’ will be {1, 0, 1, 1}. Thus the index of the fake coin is 1.
'''

'''
Constraints:- 
 1 <=  ‘T’ <= 10^5
 2 <= ‘N’ <= 10^5
 0 <= ‘C[i]’ <= 1
 0 <= ‘sum[i]’ <= ‘N-1’
 Sum of ‘N’ for all testcases <= 10^5
 There is exactly one ‘0’ in ‘C’.
 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
2
4
1 2 2 3
5
1 2 3 4 4

Sample Output 1:
2
4   

Explanation of sample output 1:

For Test 1:
‘sum’ = {1, 2, 2, 3}
‘C’ = {1, 1, 0, 1}
Index of the fake coin is 2.

For Test 2:
‘sum' = {1, 2, 3, 4, 4}
‘C’ = {1, 1, 1, 1, 0}
Index of the fake coin is 4.
'''

'''
Sample Input 2:- 
3
3
1 2 2
3
1 1 2
3
0 1 2  

Sample Output 2:
2
1
0
'''

from typing import *
def FakeCoin(sum : List[int]) -> int:
    
    '''
    Write your code here.
    '''
    
    for i in range(1, len(sum)):
        if sum[i] - sum[i - 1] != 1:
            return i
    return 0