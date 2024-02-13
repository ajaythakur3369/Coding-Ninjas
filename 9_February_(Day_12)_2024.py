'''
Task:- 
You are given a string 'str' of length 'N'.
Your task is to return the longest palindromic substring. If there are multiple strings, return any.
A substring is a contiguous segment of a string.

For example:
str = "ababc"
The longest palindromic substring of "ababc" is "aba", since "aba" is a palindrome and it is the longest substring of length 3 which is a palindrome. 
There is another palindromic substring of length 3 is "bab". Since starting index of "aba" is less than "bab", so "aba" is the answer.
'''

'''
Sample Input 1:- 
abccbc

Sample Output 1:
bccb

Explanation for input 1:
For string "abccbc",  there are several palindromic substrings such as "a", "b", "c", "cc", "bccb", and "cbc". However, the longest palindromic substring is "bccb".
'''

'''
Sample Input 2:- 
aeiou

Sample Output 2:
a
'''

'''
Constraints:- 
 1 <= |str| <= 10^3
 Time Limit: 1 sec
'''

def longestPalinSubstring(str: str) -> str:
    
    '''
    Write your code here
    '''
    
    m=0
    x=""
    for i in range(len(str)):
        for j in range(i,len(str)):
            k=str[i:j+1]
            if k==k[::-1]:
                v=len(k)
                if m<v:
                    m=v
                    x=k
    return x