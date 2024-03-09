'''
Task:- 
You have two kinds of Lego blocks (see image below) and an infinite supply of both. There is a platform of empty cells made up of 2 rows and ‘N’ columns. You must place the Lego blocks on the platform in such a way such that -
 1. Every cell on the platform is covered
 2. No two Lego blocks overlap
 3. No Lego block is placed in such a way that it goes out of the boundary of the platform.
If Lego blocks are placed such that all three conditions above are satisfied, it is called a Valid placing. Your task is to count the number of Valid ways to place the Lego blocks. Since this number might be extremely large, print it modulo (10^9+7).
'''

'''
Constraints:- 
 1 <= T <= 10
 1 <= N <= 10^5
 The sum of 'N' all test cases does not exceed 10^5.
 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
2
1
3

Sample Output 1:
1
5

Explanation for Sample Input 1:
For case 1:
The only valid placing for ‘N’ = 1 is just one blue Lego block placed vertically.

For Case 2:
The 5 valid placing for ‘N’ = 3 are shown below
'''

'''
Sample Input 2:- 
2
2
5

Sample Output 2:
2
2
24
'''

'''
    Time Complexity: O(N)
    Space Complexity: O(N)
    where 'N' is the number of columns
'''

def countWays(n):
    mod = 10 ** 9 + 7
    
    '''
    f(i) - Number of ways to place in i columns such that fully covered.
    p(i) -  Number of ways to place i columns such that partially covered.
    '''
    
    f = [0] * (n + 1)
    p = [0] * (n + 1)
    
    '''
    Base case.
    '''
    
    f[0] = f[1] = 1

    for i in range (2, n + 1):
        f[i] = (f[i - 2] + f[i - 1] + 2 * p[i - 1]) % mod
        p[i] = (f[i- 2] + p[i - 1]) % mod
    return f[n]