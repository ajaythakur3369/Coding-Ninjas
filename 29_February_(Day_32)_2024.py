'''
Task:- 
Ben Tennyson recently joined Coding Ninjas to become better at competitive programming.
To check whether Ben is seriously studying in Coding Ninjas or not, Gwen challenged Ben to solve a problem and Ben accepts the challenge of Gwen.
Gwen gives Ben an undirected graph of ‘N’ nodes numbered from 0 to ‘N - 1’ having ‘M’ edges. The task of Ben is to check whether the graph given by Gwen is a tree or not.
As Ben is busy fighting with Evil doers so he asked you to solve this problem.
'''

'''
Constraints:- 
 1 <= T <= 5
 1 <= N <= 5000
 1 <= M <= min(5000, N*(N-1)/2)
 1 <= U, V<= N - 1
'''

'''
Sample Input 1:- 
2
7 6
0 1
0 4
1 2
1 3
4 5
4 6
3 3
0 1
0 2
1 2

Sample Output 1:
1 
0

Explanation For Sample Input 1:
Test Case 1:  
The given graph is shown below. 
The above graph is a connected graph with no cycles. Hence this graph is a tree. So we need to print 1.

Test Case 2: 
The given graph is shown below.
Above graph is a connected graph but it contains a cycle : 0 -> 1 -> 2 .Hence this graph is not a tree. So we need to print 0.
'''

'''
Sample Input 2:- 
2
4 3
0 1
0 2
3 2
5 5
0 1
0 3
2 1
2 3
1 4

Sample Output 2:
1
0
'''

from os import *
from sys import *
from collections import *
from math import *

def createGraph(edges, n):
    lis = [[] for _ in range(n)]

    for s, e in edges:
        lis[s].append(e)
        lis[e].append(s)
    return lis

def isGraphTree(n: int, edgeList: list):
    q = deque()
    if n <= 2:
        return True

    visited = set()
    q.append((0, -1))
    adjList = createGraph(edgeList, n)

    while q:
        node, parent = q.popleft()
        visited.add(node)

        for nbr in adjList[node]:
            if nbr in visited:
                if nbr == parent:
                    continue
                else:
                    return False
            else:
                q.append((nbr, node)) 
    return True
    q.append((0, -1))