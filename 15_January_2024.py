'''
5. What will be the output of this code?
'''

class Base:
    def __init__(self):
        self.multiply(10)
        print(self.i)

    def multiply(self, I):
        self.i = 5 * I

class Derived(Base):
    def __init__(self):
        super().__init__()

    def multiply(self, I):
        self.i = 3 * I

obj = Derived()

'''
Output:- 30 
'''