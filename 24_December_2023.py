'''
1. What will be the output of the following Python code?
'''

class ZeroDenominatorError(ZeroDivisionError):
    pass

try:
    a = 10
    b = 5
    if b == 0:
        raise ZeroDenominatorError()
    c = a / b
except ZeroDivisionError:
    print('Zero Division Error occurred', end=' ')
except ZeroDenominatorError:
    print('Zero Denominator Error occurred', end=' ')
else:
    print('else works')

z = ZeroDenominatorError()

'''
Output:- else works
'''

'''
2. Which of the following conditions is required for a deadlock to be possible?
Answer:- all of the mentioned (mutual exclusion, a process may hold allocated resources while awaiting the assignment of other resources, no resource can be forcibly removed from a process holding it)
'''

'''
3. How many access modifiers are available in Java?
Answer:- 4
'''

'''
4. A shopkeeper gives 3 successive discounts of 20%, 30% and 50%. What is the equivalent total single discount? 
Answer:- 72%
'''

'''
5. A while loop in Java executives the statements at least once even if the condition is not satisfied.
Answer:- False
'''











