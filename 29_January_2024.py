'''
Task:- 
Write a function that calculates the corresponding day of the week for any particular date in the past or future.

For example, for the date 28th August 2020 happens to be Friday. Hence the expected output will be Friday.
'''

'''
Constraints:- 
 1 <= T <= 10^5
 1 <= Day <= 31
 1 <= Month <= 12
 1 <= Year <= 2,000,000
 Time Limit : 1 sec.
'''

'''
Sample Input 1:- 
4
28 8 2020
20 4 2033
29 2 1920
27 4 1999

Sample Output 1:
Friday
Wednesday
Sunday
Tuesday

Explanation to Sample Input 1:
It's Friday on 28th August 2020
It's Wednesday on 20th April 2033
It's Sunday on 29th February 1920
It's Tuesday on 27th April 1999
'''

'''
Sample Input 2:- 
1
28 2 1994

Sample Output 2:
Monday

Explanation to Sample Input 2:
It's Monday on 28th February 1994
'''

import datetime

class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        if m < 3:
            m += 12
            y -= 1

        century = y // 100
        year_of_century = y % 100

        h = (d + 13 * (m + 1) // 5 + year_of_century + year_of_century // 4 + century // 4 + 5 * century) % 7

        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[h]

def takeInput():
    day_month_year = list(map(int, input().strip().split(" ")))
    day = day_month_year[0]
    month = day_month_year[1]
    year = day_month_year[2]
    return day, month, year

t = int(input().strip())
for i in range(t):
    day, month, year = takeInput()
    solution = Solution()
    print(solution.dayOfTheWeek(day, month, year))
