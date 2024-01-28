'''
5. What will be the output of the following Python code?
'''

x = 1

def fun():
    global x
    x = x + 1

fun()
print(x)

'''
Output:- 2 
'''