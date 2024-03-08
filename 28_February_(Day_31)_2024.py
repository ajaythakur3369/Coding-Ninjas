'''
Task:- 
You are given an arbitrary tree consisting of 'N' nodes numbered from 0 to 'N' - 1. You need to find the total number of elements in all the subtrees of the given tree. In other words, given a generic tree, find the count of elements in the subtrees rooted at each node.

A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T. The subtree corresponding to the root node is the entire tree. 
'''

'''
Constraints:- 
 1 <= T <= 100
 1 <= N, E <= 10^4
 0 <= U,V < N 
 Time Limit: 1sec
'''

'''
Sample Input 1:- 
1
7 
0 1
0 3
0 4
1 5
3 2
3 6

Sample Output 1:
7 2 1 3 1 1 1 

Explanation for sample input 1:
The subtrees rooted at 5, 2, 6, 4 have 1 node each.
The subtree rooted at 1 has 2 nodes.
The subtree rooted at 3 has 3 nodes.
The subtree rooted at 0 has 7 nodes.
Hence, the output is {1, 1, 1, 1, 2, 3, 7}.
'''

'''
Sample Input 2:- 
1
3 
0 1
0 2

Sample Output 2:
1 1 3
'''

def dfs(curr, par, adj, ans):
    ans[curr] = 1
    for next in adj[curr]:
        if next != par:
            ans[curr] += dfs(next, curr, adj, ans)
    return ans[curr]

def countNodesInAllSubtrees(n, adj):
    ans = [0] * n
    dfs(0, -1, adj, ans)
    return ans