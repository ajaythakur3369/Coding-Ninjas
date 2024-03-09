'''
Task:- 
The Ultimate Ninja Ankush, has prepared a test for all of his fellow Ninja students, but since he is the Ultimate Ninja, he does not like cheating, and since his students are also ninjas, they broke some chairs in the dojo while practicing their moves.

The class consists of ‘M’ * ‘N’ seats, represented in a matrix ‘SEATS’. Among the seats, some of the seats are broken. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character, denoting that the seat can be occupied. A Ninja can’t sit in a broken seat.

Ankush wants to avoid cheating at any cost. According to his observations, a student can see the answers of four neighboring students sitting next to the left, right, upper left, and upper right, but they cannot see the answers of the student sitting directly in front or behind him. Ankush is very busy so he wants to use the dojo to the fullest. More formally he wants to know the maximum number of ninja students that can be placed in the dojo.

For example:
Given:
‘M’ = 3, ‘N’ = 3.
‘SEATS’ = {
   {‘.’, ‘.’, ‘.’},
   {‘#’,’#’, ‘#’},
   {‘.’,’.’,’.’} 
   }
The answer will be 4, since 4 students can be placed at the four corners, i.e. (0,0), (2,2), (2,0), and (0,2) such that no cheating is possible.
'''

'''
Constraints:-
 1 <= ‘T’ <= 10
 1 <= ‘N’ <= 10
 1 <= ‘M’ <= 10
 Time Limit: 1sec.
'''

'''
Sample Input 1:- 
2
3 3
. . .
# # #
. . .
2 4
# . # . 
# # . .

Sample Output 1:
4
3  

Explanation of the Sample Input 1:
In the first test case, The answer will be 4, since 4 students can be placed at the four corners, i.e. (0,0), (2,2), (2,0), and (0,2) such that no cheating is possible.
In the second test case, The answer will be 3, since we can place 3 students at 3 different places, i.e. (0,1), (0,3), (1,3), such that no cheating is possible. 
'''

'''
Sample Input 2:- 
2
3 3
. . . 
# . # 
# . . 
2 4
. # # # 
# . . . 

Sample Output 2:
3
2
'''

'''

    Time Complexity : O(M * (4 ^ N)).
    Space Complextiy : O(M * (2 ^ N)).
    Where 'M' is the number of rows,
    and 'N' is the number of columns.

'''

import sys

def countBits(n):
    s = str(bin(n))
    c = 0
    for i in s:
        if i == "1":
            c += 1
    return c

def maxStudents(seats):
    m = len(seats)
    n = len(seats[0])
    validity = []
    
    '''
    Parsing the seats into masks.
    '''
    
    for i in range(m):
        cur = 0
        for j in range(n):
            if (seats[i][j] == '.'):
                cur = cur ^ (1 << j)
        validity.append(cur)
    dp = [[-1 for j in range(1 << n)] for i in range(m + 1)]
    dp[0][0] = 0
    for i in range(1, m + 1):
        valid = validity[i - 1]
        
        '''
        Checking all possible combinations
        of seating students at valid positions.
        '''
        
        for j in range(1 << n):
            
            '''
            1. (j & valid) == j: check if j is a subset of valid.
            2. !(j & (j >> 1)): check if there is no adjancent students in the row.
            '''
            
            if (j & valid) == j and (j & (j >> 1)) == 0:
                for k in range(1 << n):
                    
                    '''
                    !(j & (k >> 1)): no students in the upper left positions
                    !((j >> 1) & k): no students in the upper right positions
                    dp[i - 1][k] != -1: the previous state is valid
                    '''
                    
                    if ((j & (k >> 1)) == 0 and ((j >> 1) & k) == 0 and dp[i - 1][k] != -1):
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + countBits(j))

    '''
    The answer is the maximum among all dp[m][mask].
    '''
    
    ans = -sys.maxsize -1
    for i in range(1 << n):
        ans = max(ans, dp[m][i])
    return ans
