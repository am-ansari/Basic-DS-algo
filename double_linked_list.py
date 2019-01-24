# -*- coding: utf-8 -*-

class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.prev_node = None
        self.next_node = None
        

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.prev_node = a
b.next_node = c
c.prev_node = b
c.next_node = d
d.prev_node = c
d.next_node = e
e.prev_node = d

curr = a
while curr:
    print(curr.value)
    curr = curr.next_node
    
    



        