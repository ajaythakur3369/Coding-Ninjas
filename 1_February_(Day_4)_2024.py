'''
Task:- 
You are given an array containing 'N' points in the plane. The task is to find out the distance of the closest points.

Note :
Where distance between two points (x1, y1) and (x2, y2) is calculated as [(x1 - x2)^2] + [(y1 - y2)^2].
'''

'''
Constraints:- 
 2 <= 'N' <= 10^5
 -10^5 <= 'x' <= 10^5 
 -10^5 <= 'y' <= 10^5
 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
5
1 2
2 3
3 4
5 6
2 1

Sample Output 1:
2

Explanation of Sample Output 1:
We have 2 pairs which are probable answers (1, 2) with (2, 3) and (2, 3) with (3, 4). The distance between both of them is equal to 2.
'''

'''
Sample Input 2:- 
3
0 0
-3 -4
6 4

Sample Output 2:
25

Explanation of Sample Output 1:
If we choose the pairs (0, 0) and (-3, -4), the distance between them is 3^2 + 4^2 = 25. This is the optimal answer for this test case.
'''

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

'''
Point class for 
2-D points
'''

class point:
    def __init__(self, x, y) :

        self.x = x
        self.y = y

def closestPair(cordinates, n) :
    
    '''
    Your code here
    return square of minimum distance between n points
    '''
    
    arr = [(point.x, point.y) for point in cordinates]

    '''
    Sort based on X-coordinate
    '''
    
    arr.sort(key=lambda x: x[0])
    result = float('inf')

    for i in range(1, n):
        x1, y1 = arr[i - 1]
        x2, y2 = arr[i]
        result = min(result, (x2 - x1)**2 + (y2 - y1)**2)

    '''
    Sort based on Y-coordinate
    '''
    
    arr.sort(key=lambda x: x[1])
    for i in range(1, n):
        x1, y1 = arr[i - 1]
        x2, y2 = arr[i]
        result = min(result, (x2 - x1)**2 + (y2 - y1)**2)
    return result

'''
Taking inpit using fast I/O
'''

def takeInput() :
    n = int(input().strip())
    if n == 0 :
        return list(), n
    cordinates = [point(0,0) for i in range(n)]
    for i in range(n) :
        arr = list(map(int,stdin.readline().strip().split(" ")))
        cordinates[i] = point(arr[0], arr[1])
    return cordinates, n

'''
main
'''

cordinates, n = takeInput()
print(closestPair(cordinates, n))