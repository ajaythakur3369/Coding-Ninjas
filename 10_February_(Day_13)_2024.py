'''
Task:- 
You are given an input string 'S'. Your task is to find and return all possible permutations of the input string.

Note:
1. The input string may contain the same characters, so there will also be the same permutations.
2. The order of permutation does not matter.
'''

'''
Sample Input 1:- 
cba

Sample Output 1:
abc
acb
bac
bca
cab
cba

Explanation for Sample Output 1:
All the possible permutations for string "cba" will be "abc", "acb", "bac", "bca", "cab" and "cba".
'''

'''
Sample Input 2:- 
xyx

Sample Output 2:
xyx
xxy
yxx
yxx
xyx
xxy

Explanation for Sample Output 2:
All the possible permutations for string "xyx" will be "xyx", "xxy", "yxx", "yxx", "xyx" and "xxy". Here, all three permutations "xyx", "yxx", "xxy" are repeating twice but we need to print all the possible permutations and hence we are printing them twice..
'''

from os import *
from sys import *
from collections import *
from math import *

def findPermutations(s):
    string = list(s)
    n = len(string)
    res = []
    def backtrack(start):
        if start == n:
            res.append("".join(string))
            return
        for i in range(start, n):
            string[start], string[i] = string[i], string[start]
            backtrack(start + 1)
            string[start], string[i] = string[i], string[start] 
    backtrack(0)
    return res