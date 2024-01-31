'''
1. Let A be a square matrix of size n x n. What is the expected output?
'''

C = 100
for i = 1 to n do
    for j = 1 to n do {
        Temp = A[i][j] + C
        A[i][j] = A[j][i]
        A[j][i] = Temp - C
    }

for i = 1 to n do
    for j = 1 to n do
        Output(A[i][j]);

'''
Output:- The matrix A itself
'''

'''
2. A word and number arrangement machine when given an input line of words and numbers rearranges them by following a particular rule in each step. The following is an illustration of input and rearrangement.

Input: british 32 71 greece firangi spanish 65 84
Step I spanish british 32 71 greece firangi 65 84
Step II spanish 84 british 32 71 greece firangi 65
Step III spanish 84 greece british 32 71 firangi 65
Step IV spanish 84 greece 71 british 32 firangi 65
Step V spanish 84 greece 71 firangi british 32 65
Step VI spanish 84 greece 71 firangi 65 british 32
and Step VI is the last step of the rearrangement. As per the rules followed in the above steps, find out in the following question the appropriate step for the given input.

Step III of an input is: ‘yeast 92 umbrella 15 23 slate hanger 67’.
How many more steps will be required to complete the rearrangement?
'''

'''
Answer:- 4
'''

'''
3. SQL Views are also known as? 
'''

'''
Answer:- Virtual tables
'''

'''
4. Suppose list is [3, 4, 5, 20, 5, 25, 1, 3].
list.extend([34, 5])
print(list)
'''

list = [3, 4, 5, 20, 5, 25, 1, 3]
list.extend([34, 5])
print(list)

'''
Output:- [3, 4, 5, 20, 5, 25, 1, 3, 34, 5]
'''

'''
5. A and B are two alloys of gold and copper prepared by mixing metals in the ratios 7 : 2 and 7 :11 respectively. If equal quantities of the alloys are melted to form a third alloy C, the ratio of gold and copper in C will be
'''

'''
Answer:- 7 : 5
'''
