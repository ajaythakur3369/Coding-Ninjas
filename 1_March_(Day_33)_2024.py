'''
Task:- 
You’re given a board of length 'L' and width 'W'. Your task is to break this board into 'L' * 'W' smaller squares, such that the total cost involved in breaking is the minimum possible.
'''

'''
Constraints:- 
 1 <= T <= 10
 2 <= L, W <= 10 ^ 4
 1 <= costL[i], costW[i] <= 10 ^ 5
 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
1
3 3
1 2
2 1

Sample Output 1:
11

Explanation of Sample Input 1:
Start by cutting the vertical column with cost = 2, hence cost becomes 2. Then make two cuts at the horizontal row with the cost = 2, Cost = 2*2 + 2 =6. Then vertically cut two columns with cost = 2, Cost = 6 + 1*2 = 8. Finally make three horizontal cuts with cost = 1. Final cost becomes 8 + 1*3 = 11.
'''

'''
Sample Input 2:- 
1
2 2
2
1

Sample Output 2:
4

Explanation of Sample Input 2:
In this case, we’ll be doing a total of 2 cuts. In the first cut, we’ll be cutting the first segment and our cost will now be 1*2 = 2 and in the second and the final cut, we’ll be cutting 2 segments each of cost one. Hence our final cost be 2 + 2*1 = 4.
'''

def minimumCost(row, column, l, w):
	
	'''
	Write your code here
	Return an integer
	'''
	
    row.sort()
    column.sort()
    i = l - 2
    j = w - 2
    v = 1
    h = 1
    ans = 0

    while i >= 0 and j >= 0:
        if row[i] > column[j]:
            ans += row[i] * v
            i -= 1
            h += 1

        else:
            ans += column[j] * h
            j -= 1
            v += 1

    while i >= 0:
        ans += row[i] * v
        i -= 1
        h += 1

    while j >= 0:
        ans += column[j] * h
        j -= 1
        v += 1
    return ans