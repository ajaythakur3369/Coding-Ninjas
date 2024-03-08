'''
Task:- 
You are given an array, your task is to find the maximum sum of absolute difference of adjacent numbers of any permutation of the given array.

Example:
The given array is {3, 6, 8, 4, 5}. So you have to consider all the permutations of this array like one of the permutations of this array is {6, 3, 5, 4, 8}. For this permutation answer will be sum of absolute difference of adjacent elements that is maxSum = |6-3| + |3-5| + |5-4| + |4-8| + |8-6| = 12 and for another permutation, say {3, 8, 4, 6, 5}, maxSum = |3-8| + |8-4| + |4-6| + |6-5| + |5-3| = 14. In this case, it will be the maximum of all permutations. So the answer will be 14.
'''

'''
Sample Input 1:- 
2
4
1 2 8 3
5
1 2 3 4 5

Sample Output 1:
16
12

Explanation of The Sample Input 1:
For the first test case:
The given array is : {1,2,8,3} for this array the maxSum will be of the permutation {1,8,2,3} which gives us maxSum = |1-8| + |2-8| + |8-3| + |3-1| = 16. So, we will return 16.  

For the second test case:
The given array is : {1,2,3,4,5} for this array the maxSum will be of the permutation {3,4,2,5,1} which gives us maxSum = |3-4| + |4-2| + |2-5| + |5-1| + |1-3| = 12. So, we will return 16. 
'''

'''
Sample Input 2:- 
2
6
3 4 2 9 1 5
2
1 3
Sample Output 2:
24
4
'''

def maxAbsSum(arr, n):
    
    '''
    Write your code here.
    '''
    
    arr.sort()
    left, right, res = 0, n - 1, 0
    front = True
    while left <= right:
        res += abs(arr[right] - arr[left])
        if front:
            left += 1
        else:
            right -= 1
        front = not front
    if n % 2 != 0:
        res += (arr[left - 1] - arr[0])
    else:
        res += (arr[left] - arr[0])
    return res