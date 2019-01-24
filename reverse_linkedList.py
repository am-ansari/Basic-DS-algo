# -*- coding: utf-8 -*-

class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        
def reverse(head):
    current_node = head
    previous_node, next_node = None, None
    while current_node:
        next_node = current_node.nextnode
        current_node.nextnode = previous_node
        previous_node = current_node
        current_node = next_node

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)

#print(d.nextnode.value)

reverse(a)
 
print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)
 
#print(a.nextnode.value)      