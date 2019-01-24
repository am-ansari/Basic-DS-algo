# -*- coding: utf-8 -*-

class Stack(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
9

    
s = Stack()
print(s.isEmpty())
s.push('abc')
s.push(2)
s.push('d')
s.push(4)
s.push(9)
print(s.items)
print(s.isEmpty())
print(s.size())
print(s.pop())
print(s.size())
print(s.items)
print("-"*20)

class Queue(object):
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()    
        
    def size(self):
        return len(self.items)
    
q = Queue()   
print(q.isEmpty())
q.enqueue('abc')
q.enqueue(2)
q.enqueue('d')
q.enqueue(4)
q.enqueue(9)
print(q.items)
print(q.isEmpty())
print(q.size())
print(q.dequeue())
print(q.size()) 
print(q.items)
print("-"*20)

class Deque(object):
    
    def __init__(self):
        self.items = []
   
    def isEmpty(self):
        return self.items == []
    
    def add_front(self,item):
        self.items.insert(0,item)
    
    def remove_front(self):
        return self.items.pop(0)
        
    def add_rear(self, item):
        self.items.append(item)
        
    def remove_rear(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)