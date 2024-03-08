'''
Task:- 
In a magic event, you are given ‘N’ bags, each bag containing ‘A[i]’ chocolates. In one unit of time, you can choose any bag ‘i’ and eat all the chocolates ‘A[i]’ in that bag and then the magician fills the ith bag with floor(‘A[i]’ / 2) chocolates. Your task is to find the maximum number of chocolate you can eat in ‘K’ units of time.
Since the answer could be large, return answer modulo 10^9 + 7.

For Example:
For the array [ 4, 7, 9, 10] and ‘k’=2
In the first step, we can choose the last bag. So the answer will be 10 and the array will be [4, 7, 9, 5].
In the second step, we can choose the second last bag. So the answer will be 19 and the array will be [4, 7, 4, 5].
So the final output will be 19.
'''

'''
Constraints:- 
 1 <= T <= 100
 1 <= N <= 10^5
 1 <= ARR[i] <= 10^5
 It is guaranteed that the sum of ‘N’ over all test cases doesn’t exceed 10^5.
 Time Limit: 1 sec.
'''

'''
Sample Input 1:- 
2
4 1
3 8 2 4
4 2
10 4 7 22

Sample Output 1:
8
33

Explanation For Sample Output 1:
For the first test case,
In the first step, we can choose the second bag. So the answer will be 8 and the array will be [3, 4, 2, 4].
So, the final answer will be 8.

For the second test case,
In the first step, we can choose the last bag. So the answer will be 22 and the array will be [10, 4, 7, 11].
In the second step, we can choose the last bag. So the answer will be 33 and the array will be [10, 4, 7, 5].
So, the final answer will be 33.
'''

'''
Sample Input 2:- 
2
5 3
3 6 10 12 8
4 1
2 10 4 3
Sample Output 2:
30
10
'''

from os import *
from sys import *
from collections import *
import math
import heapq

def maximumChocolates(arr, k):
    
    '''
    Write your code here.
    '''
    
    heap=[]
    for i in arr:
        heapq.heappush(heap,-i)
    Sum=0
    while k!=0:
        a=-heapq.heappop(heap)
        Sum+=a
        a=math.floor(a/2)
        heapq.heappush(heap,-a)
        k-=1
    return Sum