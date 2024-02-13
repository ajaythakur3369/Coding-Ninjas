'''
Task:- 
You are given a non-decreasing array 'arr' consisting of 'n' integers and an integer 'x'. You need to find the first and last position of 'x' in the array.

Note:
1. The array follows 0-based indexing, so you need to return 0-based indices.
2. If 'x' is not present in the array, return {-1 -1}.
3. If 'x' is only present once in the array, the first and last position of its occurrence will be the same.

Example:
Input: arr = [1, 2, 4, 4, 5],  x = 4

Output: 2 3

Explanation: The given array’s 0-based indexing is as follows:
 1      2     4     4     5
 ↓      ↓     ↓     ↓     ↓
 0      1     2     3     4

So, the first occurrence of 4 is at index 2, and the last occurrence of 4 is at index 3.
'''

'''
Sample Input 1:- 
5
-10 -5 -5 -5 2
-5

Sample Output 1:
1 3

Explanation for Sample Input 1:
The given array’s 0-based indexing is as follows:
-10    -5    -5    -5     2
 ↓      ↓     ↓     ↓     ↓
 0      1     2     3     4

So, the first occurrence of -5 is at index 1, and the last occurrence of -5 is at index 3.
'''

'''
Sample Input 2:- 
4
1 2 3 4
-1

Sample Output 2:
-1 -1

Explanation for Sample Input 2:
The given array 'arr' is:[1, 2, 3, 4] and 'x' = -1.
In this case 'x' is not present in the array.
Hence, we return {-1,-1}.
'''

'''
Constraints:- 
 1 <= n <= 10^4
 -10^9 <= arr[i] <= 10^9
 -10^9 <= x <= 10^9
 Time Limit: 1sec
'''

'''
Expected Time Complexity:- 
Try to solve the problem in O(log(N)) time complexity.
'''

def searchRange(arr: [int], x: int) -> [int]:
    
    '''
    Write your code here.
    '''
    
    lst=[]
    for i in range(len(arr)):
        if arr[i]==x:
            lst.append(i)
            break
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==x:
            lst.append(abs(i))
            break
    if len(lst)==0:
        return [-1,-1]
    return lst