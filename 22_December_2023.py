'''
4. What will be the output of the following Python code?
'''

def fun(a, b=0):
    print(a + b)

# Driver’s code
fun(2)

''''
Output:- 2
'''

'''
5. What will be the output of the code?
'''

class One:
    pass

class Two(One):
    pass

obj = Two()
isinstance(obj, One)

'''
Output:- True
'''