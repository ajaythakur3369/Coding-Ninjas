'''
Task:- 
Monk's favorite game is Football and his favorite club is "Manchester United". Manchester United has qualified for the Champions League Final which is to be held at the Wembley Stadium in London. So, he decided to go there and watch his favorite team play. After reaching the stadium, he saw that many people have lined up for the match tickets. He knows that there are 'M' rows in the stadium with different seating capacities. They may or may not be equal. The price of the ticket depends on the row. If the row has 'K' vacant seats, then the price of the ticket will be 'K' pounds. Now, every football fan standing in the line will get a ticket one by one.
You are given 'N' number of fans waiting for the tickets and seating capacities of different rows. The club wants to gain maximum pounds with the help of ticket sales.
Your task is to print the maximum possible pounds that the club will gain with the help of ticket sales.
'''

'''
Constraints:- 
 1 <= 'M' <= 5 * 10^5 
 1 <= 'N' <= 10^9 
 1 <= 'VACANT_SEATS[i]' <=10^9 

 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
4 5 
2 3 1 4

Sample Output 1:
14

Explanation For Sample Input 1:
We have 5 people waiting in line and the possible prices are 2, 3, 1 and 4 (in pounds). 
The 1st person is given a ticket in the 4th row worth 4 pounds. Updated possible prices are 2, 3, 1, 3 (in pounds).
The 2nd person is given a ticket in the 4th row worth 3 pounds. Updated possible prices are 2, 3, 1, 2 (in pounds).
The 3rd person is given a ticket in the 2nd row worth 3 pounds. Updated possible prices are 2, 2, 1, 2 (in pounds).
The 4th person is given a ticket in the 2nd row worth 2 pounds. Updated possible prices are 2, 1, 1, 2 (in pounds).
The 5th person is given a ticket in the 1st row worth 2 pounds. Updated possible prices are 1, 1, 1, 2 (in pounds).

Hence, the total money collected is ( 4 + 3 + 3 + 2 + 2 ) = 14 pounds. 
'''

'''
Sample input 2:-
6 9
1 5 7 3 9 12

Sample output 2:
81
'''

from os import *
from sys import *
from collections import *
from math import *

'''
    Time Complexity: O(M * logM)
    Space Complexity: O(1)
    Where M is the number of rows.
'''

def footballGame(vacantSeats, m, n):

    vacantSeats.sort()
    ans = 0
    c = 1
    for i in range(len(vacantSeats) - 1, -1, -1):
        if n <= 0 or i == 0:
            break
        diff = vacantSeats[i] - vacantSeats[i - 1]
        if n >= diff * c:
            ans += summ(vacantSeats[i - 1] + 1, diff) * c
        else:
            x = int(n / c)
            maxx = vacantSeats[i - 1] + diff
            if x > 0:
                ans += summ(maxx - x + 1, x) * c
                n -= x * c
                maxx -= x

            ans += maxx * n
            n = 0
        n -= diff * c
        c += 1
        
    if n > 0:
        c -= 1
        x = int(n / c)
        maxx = vacantSeats[0]
        if x > 0:
            ans += summ(maxx - x + 1, x) * c
            n -= x * c
            maxx -= x
        ans += maxx * n
    return ans

def summ(a, n):
    a2 = a * 2
    ans = int(n * (a2 + n - 1) / 2)
    return ans
