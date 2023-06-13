# Linked List
# Creating a single node
# So this node will be the head and tail node.
class Node:
    def __init__(self,value):
        self.value = value; # Assigning Value
        self.next = None; # Tail
new_node = Node(10);
print(new_node); # Shows address of the nodes memory location.
print(new_node.next); # Shows the address of the next node. None in case of last node.
print(new_node.value); # Shows the value of the node

