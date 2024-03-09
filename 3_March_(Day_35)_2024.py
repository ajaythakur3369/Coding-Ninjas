'''
Task:- 
Given an integer 'N', your task is to write a program that returns all the divisors of 'N' in ascending order.

For example:
'N' = 5.
The divisors of 5 are 1, 5.
'''

'''
Sample Input 1:- 
10

Sample Output 1:
1 2 5 10

Explanation of Sample Input 1:
The divisors of 10 are 1,2,5,10.
'''

'''
Sample Input 2:-
6

Sample Output 2:
1 2 3 6

Explanation of Sample Input 2:
The divisors of 6 are 1, 2, 3, and 6.
'''

'''
Constraints:- 
 1 <= 'N' <= 10^5 
'''

from typing import List
def printDivisors(n: int) -> List[int]:
    
    '''
    Write your code here
    '''
    
    i = 1
    front = []
    back = []
    while i*i<=n:
        if n%i==0:
            front.append(i)
            if i!=n//i:
                back.append(n//i)
        i+=1
    return front+back[::-1]