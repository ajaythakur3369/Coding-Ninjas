'''
Task:- 
Ninja has ‘N’ beautiful paintings labeled from 1 to N.He has to go to an exhibition to showcase ‘K’ paintings. Now, he is confused about which combinations of paintings he should choose.He wants to make all possible combinations of these ‘N’ paintings. Can you help Ninja to make all the possible combinations of N paintings?

For Example:
For the given if N is 4 and K is 3,the possible combinations are [1,2,3] , [1,2,4] , [2,3,4],[1,3,4] .
'''

'''
Constraints:-
 1 <= T <= 10
 1 <= N <= 20.
 1 <= K <= N.
 Time limit: 1 sec
'''

'''
Sample Input 1:-
2
4 3
4 1 

Sample Output 1:
1 2 3
1 3 4
1 2 4
2 3 4
1
2
3
4 

Explanation of sample input 1:
For the first test case,
The possible combinations are [1,2,3] , [1,2,4] , [2,3,4],[1,3,4]. 

For the second test case:
The possible combinations are [1],[2],[3],[4]. 
'''

'''
Sample Input 2:- 
2
3 3
4 2

Sample Output 2:
1 2 3
1 2 
1 3
1 4
2 3 
2 4
3 4
'''

from os import *
from sys import *
from collections import *
from math import *
from typing import *
def combinations(n :int,k :int) -> List[List[int]]:
    
    '''
    Write your code here.
    '''
    
    res=[]
    def f(idx,comb):

        if len(comb)==k:
            res.append(comb.copy())
            return 
        for i in range(idx,n+1):
            comb.append(i)
            f(i+1,comb)
            comb.pop()
        
    f(1,[])
    return res
