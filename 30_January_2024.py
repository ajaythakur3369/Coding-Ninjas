'''
3. What will be the output of the following code?
'''

class Student:
    def store_details(self):
        self.age = 60
        self.name = ‘Parikh’
    def print_details(self):
        print(self.name, end=” ”)
        print(self.age)

s = Student()
s.store_details()
s.print_details()

'''
Output:- Parikh 60
'''

'''
4. What is the output of the following for loop and range() function?
'''

for num in range(2,-5,-1):
    print(num, end=", ")

'''
Output:- 2, 1, 0, -1, -2, -3, -4,
'''

'''
5. What is the return type of a method that doesn't return any value?
'''

'''
Answer:- void
'''








