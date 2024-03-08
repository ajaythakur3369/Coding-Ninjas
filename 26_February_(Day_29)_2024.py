'''
Task:- 
You are given two arrays/lists ‘A’ and ‘B’ of size ‘N’ each. You are also given an integer ‘K’.
You must return ‘K’ distinct maximum and valid sum combinations from all the possible sum combinations of the arrays/lists ‘A’ and ‘B’.
Sum combination adds one element from array ‘A’ and another from array ‘B’.

For example:
A : [1, 3] 
B : [4, 2] 
K: 2

The possible sum combinations can be 5(3 + 2), 7(3 + 4), 3(1 + 2), 5(1 + 4). 
The 2 maximum sum combinations are 7 and 5. 
'''

'''
Sample Input 1:- 
3 2
1 3 5
6 4 2

Sample Output 1:
11 9

Explanation of Sample Output 1:
For the given arrays/lists, all the possible sum combinations are: 
7(1 + 6), 5(1 + 4), 3(1 + 2), 9(3 + 6), 7(3 + 4), 5(3 + 2), 11(6 + 5), 9(5 + 4), 7(5 + 2).

The two maximum sum combinations from the above combinations are 11 and 9.
'''

'''
Sample Input 2:- 
2 1
1 1
1 1
Sample Output 2:
2
Explanation of sample input 2:
For the given arrays/lists, two possible sum combinations are 2(1 + 1), and 2(1 + 1).
'''

'''
Constraints:- 
 1 <= N <= 100
 1 <= K <= N
 -10^5 <= A[i], B[i] <= 10^5
 'A[i]' and 'B[i]' denote the ith element in the given arrays/lists. 
 Time limit: 1 sec
'''

from typing import List
import heapq

def kMaxSumCombination(a: List[int], b: List[int], n: int, k: int) -> List[int]:
    
    '''
    write your code here
    '''
    
    result = []
    a.sort()
    b.sort()
    maxHeap = []

    heapq.heappush(maxHeap, (-(a[-1] + b[-1]), (n - 1, n - 1)))
    visited = set()
    visited.add((n - 1, n - 1))

    while k > 0:
        val, (i, j) = heapq.heappop(maxHeap)
        result.append(-val)
        k -= 1

        if i > 0 and (i-1, j) not in visited:
            heapq.heappush(maxHeap, (-(a[i-1] + b[j]), (i-1, j)))
            visited.add((i-1, j))
        
        if j > 0 and (i, j-1) not in visited:
            heapq.heappush(maxHeap, (-(a[i] + b[j-1]), (i, j-1)))
            visited.add((i, j-1))

    return result