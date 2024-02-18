'''
Task:- 
Ninjas is practicing problems on the linked list. He came across a problem in which he has given a linked list of ‘N’ nodes and an array ‘ARR’ of size ‘M’ that is the subset of the values present in the linked list. He has to print the number of connected components present in the array. Two values are said to be connected if they present next to each other in the linked list.
'''

'''
Constraints:- 
 1 <= T <= 10
 1 <= N <= 3*10^3
 1 <= M <= N
 The linked list consists of unique integers only.
 Time Limit: 1 sec
'''

'''
Sample Input 1:- 
2
1 3 2 4 6 5 -1
2
1 3
1 3 7 4 -1 
3
1 7 4

Sample Output 1:
1
2

Explanation For Sample Input 1:
For the first test case:
1 3 appears consecutively in the linked list. So, they are connected.  
Count: 1

For the second test case:
1 and 7 4 are connected.
Count: 2
'''

'''
Sample Input 2:- 
2
1 3 4 5 -1
4
1 3 4 5
1 2 -1
1
1

Sample Output 2:
1
1
'''

from typing import List

'''
    Following is the class structure of the Node class:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
'''

def countConnected(head, arr: List[int], m: int) -> int:
    
    '''
    write your code here
    '''
    
    i = 0  
    f,ct = 0,0
    node = head
    d = {} 
    for i in range(m) :
        d[arr[i]] = i  
    while node != None and i < m :
        if node.data in d.keys() : 
            arr[d[node.data]] = -1
            f = 1 
        else :
            if f :
                ct += 1 
            f = 0 
        node = node.next 
    if f :
        ct += 1 
    return ct