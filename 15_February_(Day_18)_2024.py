'''
Task:- 
You have been given an array ‘ARR’ that might contain duplicate elements. Your task is to find the maximum possible distance between occurrences of two repeating elements i.e. elements having the same value. If there are no duplicate elements in the array, return 0.
'''

'''
Constraints:- 
 0 <= N <= 10^6    
 -10^9 <= ARR[i] <= 10^9
 Time Limit: 1sec
'''

'''
Sample Input 1:- 
9
1 3 1 4 5 6 4 8 3

Sample Output 1:
7 

Explanation for Sample Output 1:
In the above array, the repeating elements are:- (1, 3, 4)
Distance between first and last occurrence of 1 = 2(index2 - index0)
Distance between first and last occurrence of 3 = 7(index8 - index1)
Distance between first and last occurrence of 4 = 3(index6 - index3)

So, for the above array, you must return 7, as this is the maximum possible distance between two repeating elements having the same value.
'''

'''
Sample Input 2:- 
4
1 3 2 4

Sample Output 2:
0
'''

from os import *
from sys import *
from collections import *
from math import *
from sys import stdin

def maximumDistance(arr):
    a = {}
    b = 0
    if arr is None:
        return 0
    
    for i in range(len(arr)):
        if arr[i] not in a:
            a[arr[i]] = i
        else:
            if i - a[arr[i]] > b:
                b = i - a[arr[i]]
    return b

'''
Main Code
'''

n = int(input())
if n > 0:
    arr = list(map(int, stdin.readline().strip().split()))
    ans = maximumDistance(arr)
    print(ans)
else:
    print(0)