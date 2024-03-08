'''
Task:- 
You are given a string 'exp' which is a valid infix expression.
Convert the given infix expression to postfix expression.

Example:
Input: exp = ‘3+4*8’
Output: 348*+
Explanation:
Here multiplication is performed first and then the addition operation. Hence postfix expression is  3 4 8 * +.
'''

'''
Sample Input 1:- 
3^(1+1)

Expected Answer:
311+^

Output printed on console:
311+^

Explanation of Sample Input 1:
For this testcase, we will evaluate 'b' = (1+1) first. 
Hence it's equivalent postfix expression will be "11+". 
Next we will evaluate 3^b. It's equivalent postfix expression will be "3b^". 
Replacing 'b' with it's equivalent postfix we get "311+^".
'''

'''
Sample Input 2:- 
a+b+c+d-e

Expected Answer:
ab+c+d+e-

Output printed on console:
ab+c+d+e-

Expected Time Complexity:
Try to do this in O(n).
'''

'''
Constraints:- 
 1 <= 'n' <= 5000 
 'n', is the length of EXP
 The expression contains digits, lower case English letters, ‘(’, ‘)’, ‘+’, ‘-’, ‘*’, ‘/’, ‘^’. 
 Time Limit: 1 sec
'''

def infixToPostfix(exp: str) -> str:
    
    '''
    Write your code here.
    '''
    
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3,'(':0}
    st=[]
    postfix=''
    for i in exp:
        if i=='(':
            st.append(i)
        elif i==')':
            while st[-1]!='(':
                postfix+=st.pop()
            st.pop()
        elif i in precedence:
            while st and precedence[st[-1]]>=precedence[i]:
                postfix+=st.pop()
            st.append(i)
        else:
            postfix+=i
    while st:
        postfix+=st.pop()
    return postfix