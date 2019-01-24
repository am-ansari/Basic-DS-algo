# -*- coding: utf-8 -*-

class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        
def cycle_check(node):
    nodePtrArr = []
    while node.nextnode:
        if node not in nodePtrArr:
            nodePtrArr.append(node)
            node = node.nextnode
        else:
            return True
        
    return False    
        

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a 

x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

print(cycle_check(x))
print(cycle_check(a))