'''
Task:- 
Implement a queue data structure which follows FIFO(First In First Out) property, using only the instances of the stack data structure.

Example:
Operations: 
1 5
1 10
2
3
4

Enqueue operation 1 5: We insert 5 at the back of the queue.
Queue: [5]

Enqueue operation 1 10: We insert 10 at the back of the queue.
Queue: [5, 10]

Dequeue operation 2: We remove the element from the front of the queue, which is 5, and print it.
Output: 5
Queue: [10]

Peek operation 3: We return the element present at the front of the queue, which is 10, without removing it.
Output: 10
Queue: [10]

IsEmpty operation 4: We check if the queue is empty.
Output: False
Queue: [10]
'''

'''
Sample Input 1:- 
7
1 1
1 2
1 3
2
2
2
3

Sample Output 1:
1 
2 
3
-1

Explanation of the Sample Output 1:
Here we have seven queries in total.

Query 1: Insert 1 to the back of the queue. The queue: 1 
Query 2: Insert 2 to the back of the queue. The queue: 1 2
Query 3: Insert 3 to the back of the queue. The queue: 1 2 3
Query 4: Remove element from the front:  The queue: 2 3
Query 5: Remove the element from the front:  The queue: 2 
Query 6: Remove the element from the front:  The queue : 
Query 7: As the queue is empty, returned -1.
'''

'''
Sample Input 2:- 
2
1 2
4

Sample Output 2:
false

Explanation of the Sample Output 2:
Here we have two queries in total.

Query 1: Insert 2 to the back of the queue. The queue: 2 
Query 2: IsEmpty() function returns 'false' as currently the queue is not empty.
'''

'''
Constraints:- 
 1 <= Q <= 1000
 1 <= type <= 4
 1<= data <= 10^9 
 Where 'type' represents the type of query and 'data' represents the integer to be enQueued. 
 Time limit: 1 sec
'''

class Queue:

    def __init__(self) -> None:
        
        '''
        Initialize your data structure here.
        '''
        
        self.input=[]
        self.output=[]

    def enQueue(self, val: int) -> None:
        
        '''
        Implement the enqueue() function.
        '''
        
        self.input.append(val)

    def deQueue(self) -> int:
        
        '''
        Implement the dequeue() function.
        '''
        
        if len(self.input)==0 and len(self.output)==0:
            return-1
        if len(self.output)>0:
            return self.output.pop()
        while len(self.input)>0:
            self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        
        '''
        Implement the peek() function here.
        '''
        
        if len(self.input)==0 and len(self.output)==0:
            return-1

        if len(self.output)>0:
            return self.output[-1]
        while len(self.input)>0:
            self.output.append(self.input.pop()) 
        return self.output[-1]

    def isEmpty(self) -> bool:
        return len(self.input)==0 and len(self.output)==0