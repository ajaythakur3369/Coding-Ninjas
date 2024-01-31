'''
Task:- 
Hisoka was so hungry for power that he left Phantom Troupe in search of power. He met two kids on his way, Gon and Killua. They gave him four numbers A, B, C, and M where M is a Prime Number and told him that if he can calculate A^(B^C) Mod M, he will gain a lot of powers. Hisoka is weak in coding. Can you help hisoka solve this problem of powers.

For Example:
A = 2, B = 2, C = 3, M = 5

Computing B^C gives 2^3 = 8, Now A^(B^C) = 2^8 = 256.  256 Mod 5 is 1. Hence the final answer is 1.
'''

'''
Constraints:- 
 1 <= T <= 100
 1 <= A, B, C <= 10^9
 1 < M <= 10^9 + 7
 Time limit: 1 sec
'''

'''
Sample Input 1:- 
2
3 2 3 11
5 2 2 7

Sample Output 1:
5
2

Explanation For Sample Output 1:
For the first test case, the value of 2^3 is 8 and hence the value of 3^8 is 6561. 6561 mod 11 is 5. So the final Answer is 5.

For the second test case, the value of 2^2 is 4 and hence the value of 5^4 is 625. 625 mod 7 is 2. So the final Answer is 2.
'''

'''
Sample Input 2:- 
2
3 9 4 19
55 69 21 998244353 

Sample Output 2:
18
441977229
'''

from os import *
from sys import *
from collections import *
from math import *

def mod_exp(base, exp, mod):
    if exp == 0:
        return 1

    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod

        exp = exp >> 1  
        base = (base * base) % mod

    return result

def powerOfPower(A, B, C, M):
    
    '''
    Using Fermat's Little Theorem: a^(b^c) % m == a^(b^c % (m-1)) % m
    First, we calculate B_pow_C = (b^c % (m-1))
    Then, we calculate result = (a^B_pow_C) % m
    '''

    B_pow_C = mod_exp(B, C, M - 1)
    result = mod_exp(A, B_pow_C, M)

    return int(result)
