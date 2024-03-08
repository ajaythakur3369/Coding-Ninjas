'''
Task:- 
You are given an undirected graph with ‘N’ nodes and ‘M’ edges. There are two players P1 and P2, who want to traverse the complete graph. There are three types of edges in the graph, type 1 edges can be traversed by player P1, type 2 edges can be traversed by player P2, and type 3 edges can be traversed by both P1 and P2.
You are supposed to find the maximum number of edges that can be removed from the graph so that both players P1 and P2 can reach any node of the graph.

For Example:
In the above graph, we can remove both the edges connecting node 1 and node 2(of type 1 and type 2). The graph will be fully traversable by only type 3 edges.
'''

'''
Constraints:- 
 1 <= T <= 5
 1 <= N <= 10^5
 1 <= M <= 10^5
 1 <= TYPE <= 3
 1 <= X,Y <= N 
 Where ‘T’ denotes the number of test cases, ‘N’ denotes the number of nodes in the graph, ‘M’ denotes the number of edges in the graph, “TYPE” denotes the type of edge, ‘X’ and ‘Y’ denote the nodes of the graph.
 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
2
4 5
1 1 2
2 1 2
3 4 1
3 2 4
3 3 4
3 3
3 1 2
2 2 3
1 1 3

Sample Output 1:
2
0

Explanation For Sample Input 1:
In the first test case, we can remove 2 edges connecting node 1 and node 2(refer to the example above).
In the second test case, we cannot remove any edge as removing any edge will make the graph disconnected.
'''

'''
Sample Input 2:- 
2
4 2
1 2 1
3 3 4
2 2
3 1 2
1 2 1

Sample Output 2:
-1
1

Explanation For Sample Input 2:
In the first test case, the graph is disconnected hence both the players cannot traverse all the nodes.
In the second test case, we can remove one edge of type 1.
'''

from os import *
from sys import *
from collections import *
from math import *

class UnionFind:
    def __init__(self, n):
        self.representative = list(range(n + 1))
        self.componentSize = [1] * (n + 1)
        self.components = n

    def findRepresentative(self, x):
        if self.representative[x] == x:
            return x
        self.representative[x] = self.findRepresentative(self.representative[x])
        return self.representative[x]

    def performUnion(self, x, y):
        x = self.findRepresentative(x)
        y = self.findRepresentative(y)

        if x == y:
            return 0

        if self.componentSize[x] > self.componentSize[y]:
            self.componentSize[x] += self.componentSize[y]
            self.representative[y] = x
        else:
            self.componentSize[y] += self.componentSize[x]
            self.representative[x] = y

        self.components -= 1
        return 1

    def isConnected(self):
        return self.components == 1

def removeMaxEdges(n, m, edges):
    Alice = UnionFind(n)
    Bob = UnionFind(n)
    edgesRequired = 0

    for edge in edges:
        if edge[0] == 3:
            edgesRequired += (Alice.performUnion(edge[1], edge[2]) | Bob.performUnion(edge[1], edge[2]))

    for edge in edges:
        if edge[0] == 1:
            edgesRequired += Alice.performUnion(edge[1], edge[2])
        elif edge[0] == 2:
            edgesRequired += Bob.performUnion(edge[1], edge[2])

    if Alice.isConnected() and Bob.isConnected():
        return len(edges) - edgesRequired

    return -1