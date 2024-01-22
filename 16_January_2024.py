'''
5. What will be the output of the following code?
'''

class Car:
    def __init__(self):
        self.name = "swift"
        self.maxSpeed = 150

c = Car()
c.name = "Wagon R"
c.maxSpeed = 135
print(c.name, c.maxSpeed)

'''
Output:- Wagon R 135 
'''
