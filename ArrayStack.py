import numpy as np
from Interfaces import Stack

class ArrayStack(Stack):
    '''
        ArrayStack: Implementation of the Stack interface based on Arrays. 
        All the @abstractemthods should be implemented. 
        An instance of ArrayStack has access to all the methods in ArrayStack and 
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple, 
        s = ArrayStack()
        print(s)
        print(len(s))
    '''
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        b = self.new_array(max(1, self.n * 2)) #new array with twice the capacity
        for i in range(self.n): #copy elements to a
            b[i] = self.a[i]
        self.a = b   #reassign

        '''
                    Resize the array
                '''

    def get(self, i : int) -> np.object:
        if i < 0 or i >= self.n:   #check invariant
            raise IndexError()
        return self.a[i]

    
    def set(self, i : int, x : np.object) -> object:
        if i < 0 or i >= self.n: #check invariant
            raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y
    
    def add(self, i: int, x : np.object):
        if i < 0 or i > self.n: #check precondition
            raise IndexError()
        if self.n == len(self.a):   #resize if array is full
            self.resize()
        for j in range(self.n - 1, i-1, -1):  #shift right
            self.a[j + 1] = self.a[j]
        self.a[i] = x
        self.n += 1  #increment n by 1
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''

    def remove(self, i : int) -> np.object :
        if i < 0 or i >= self.n: #check precondition
            raise IndexError()
        x = self.a[i]   #store in temporary variable
        if self.n > 1:#shift elements to the left
            self.a[i:self.n - 2] = self.a[i + 1:self.n - 1]
        self.n -= 1  #decrement n by 1
        if len(self.a) >= 3 * self.n: self.resize() #check invariant
        return x
        '''
            remove element i and shift all j > i one 
            position to the left
        '''

    def push(self, x : np.object) :
        self.add(self.n, x)
    
    def pop(self) -> np.object :
        return self.remove(self.n-1)

    def size(self) :
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        #if len(self.a) < 0: raise IndexError()
        #self.n = len(self.a)
        return self.n
        
    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
            Initialize the iterator. It is to be use in for loop
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
            Move to the next item. It is to be use in for loop
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
        




