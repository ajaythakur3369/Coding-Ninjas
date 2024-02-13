'''
Task:- 
Given a Binary Tree with integer nodes, your task is to find the maximum level sum among all the levels in the Binary Tree. The sum of any level in a tree is the sum of all the nodes present at that level.
'''

'''
Constraints:- 
 1 <= T <= 100
 1 <= N <= 1000
 -10^5 <= DATA <= 10^5 and DATA != -1    

 Where ‘N’ is the number of nodes, 'DATA' is the value of nodes in the given tree.
 Time limit: 1 sec
'''

'''
Sample Input 1:- 
1                
4 2 -5 1 3 -2 6 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 1:
8

Explanation of Sample Output 1:
The Sum of all nodes of the 0th level is 4.
The Sum of all nodes of  the1st level is  2 + (-5) = -3.
The Sum of all nodes of the 2nd level is 1 + 3 +(-2) + 6 = 8.
Hence, the maximum level sum is 8.
'''

'''
Sample Input 2:- 
1         
1 2 3 4 5 -1 8 -1 -1 -1 -1 6 7 -1 -1 -1 -1

Sample Output 2:
17

Explanation of Sample Output 2:
Maximum sum is at level 2 i.e. 4 + 5 + 8 = 17.
'''

from os import *
from sys import *
from collections import *
from math import *
from queue import Queue

'''
Binary tree node class for reference
'''

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def maxLevelSum(root):
    
    '''
    Write your code here
    '''
    
    Max=float("-inf")
    q=[root]
    while q:
        Sum=0
        Size=len(q)
        for i in range(len(q)):
            temp=q.pop(0)
            Sum+=temp.val
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        Max=max(Sum,Max)

    return Max

'''
Fast input
'''

def takeInput():
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = TreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = TreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = TreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

'''
Main
'''

t = int(input().strip())
for i in range(t):
    root = takeInput()
    maxSum = maxLevelSum(root)
    print(maxSum)