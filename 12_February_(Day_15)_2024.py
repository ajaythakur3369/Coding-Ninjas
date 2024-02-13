'''
Task:- 
Given a binary tree, convert this binary tree into its mirror tree.
A binary tree is a tree in which each parent node has at most two children.
Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.

Note:
1. Make in-place changes, that is, modify the nodes given a binary tree to get the required mirror tree.
'''

'''
Sample Input 1:- 
2
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1 
1 3 2 -1 -1 5 4 -1 -1

Sample output 1:
1 3 2 7 6 5 4 -1 -1 -1 -1 -1 -1 -1 -1 
1 2 3 4 5 -1 -1 -1 -1 -1 -1

In a mirror, objects on the left appear to be on the right, and objects on the right appear to be on the left.

Similarly, in the above figure, 

At level 1: Since only the node with value 1 is present, it stays as at root in the mirror tree as well.
At level 2: Subtree with root 2 appears on the left and the subtree with root 3 appears on the right in the actual tree, their positions are swapped in the mirror tree. Now, subtree with root 3 comes on the left and subtree with root 2 on the right.
At level 3: Nodes 6 and 7 change positions and nodes 4 and 5 also change their positions.
'''

'''
Sample Input 2:- 
1
10 12 6 -1 -1 15 4

Sample output 2:
10 6 12 4 15 -1 -1 -1 -1 -1 -1
'''

from os import *
from sys import *
from collections import *
from math import *
import queue
import sys

sys.setrecursionlimit(10**6)

'''
Following is the structure used to represent the Binary Tree Node
Following is the structure used to represent the Binary Tree Node
'''

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirrorTree(node):
    if node is not None:
        
        '''
        Recursively swap left and right nodes
        '''
        
        node.left, node.right = node.right, node.left
        mirrorTree(node.left)
        mirrorTree(node.right)

'''
Function to print the tree nodes
'''

def printTree(root):
    if root is None:
        return
    q = [root]
    while q:
        current = q.pop(0)
        if current is None:
            print("-1", end=" ")
        else:
            print(current.data, end=" ")
            q.append(current.left)
            q.append(current.right)
    print()

'''
Taking level-order input using fast I/O method
'''

def takeInput():
    levelOrder = list(map(int, input().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    nodes = [root]

    while start < length:
        current = nodes.pop(0)

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            current.left = leftNode
            nodes.append(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            current.right = rightNode
            nodes.append(rightNode)

    return root

'''
Main
'''

t = int(input())
while t:
    root = takeInput()
    mirrorTree(root)
    printTree(root)
    t = t - 1