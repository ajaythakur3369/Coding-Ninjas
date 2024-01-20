'''
1. What will be output of the following code?
'''

def fun(n):
    n = 5
    return n

n = 10
n = fun(n)
print(n)

'''
Output:- 5
'''

'''
2. What will be the output of the following statement?
'''

z = True and False
print(z)

'''
Output:- False
'''

'''
3. What will be the output of the following Python code?
'''

def fun(**kwargs):
    for key, value in kwargs.items():
        print(key, value, end=" ")

# Driver’s code
fun(company="codingninjas", location="delhi")

'''
Output:- company codingninjas location delhi 
'''

'''
4. What will be the output of the following Python code?
'''

list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)

'''
Output:- [4, 3]
'''






