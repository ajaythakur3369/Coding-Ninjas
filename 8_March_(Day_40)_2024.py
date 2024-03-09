'''
Task:- 
You are given ‘N’ characters, these characters can be used to construct words and these words can further be used to construct sentences.
Find all the distinct sentences that you can build while maintaining the relative order of these characters. Print the sentences in lexicographical order.

For Example :
If N = 3 and characters are = { a, b, c }
Then the four distinct sentences you can build:
a b c 
a bc 
ab c 
abc 
'''

'''
Constraints:- 
 1 ≤ T ≤ 10      
 1 ≤ N ≤ 15
 String ‘S’ consist of only lower case English alphabets
 Time limit: 1 sec
'''

'''
Sample Input 1:-
2
3
abc
2
xy

Sample Output 1:
a b c 
a bc 
ab c 
abc 
x y 
xy

Explanation For Sample Input 1:
For test case 1 :
There are four distinct sentences we can build from “abc” such that the order of characters doesn’t change, these sentences are:
a b c 
a bc 
ab c 
abc

For test case 2 : 
There are two distinct sentences we can build from “xy” such that the order of characters doesn’t change, these sentences are:
x y
xy
'''

'''
Sample Input 2:- 
2
1
a
2
cd

Sample Output 2:
a
c d
cd
'''

from typing import List
def allSenteces(n: int, s: str) -> List[List[str]]:
    
    '''
    write your code here
    '''
    
    def solve(ind, s, ds, ans):
        if ind >= len(s):
            ans.append(ds[:])
            return

        temp = ""
        for i in range(ind, len(s)):
            temp += s[i]
            ds.append(temp)
            solve(i + 1, s, ds, ans)
            ds.pop()

        temp = temp[:-1]

    ans = []
    ds = []
    solve(0, s, ds, ans)
    return ans