# Singly linked list
# Code has 2 parts
# 1) Node part
# 2) Linked list part
# Action: Add node to the end of the linked list

# Creating class for Node

class Node:
    # Creating initializer function to invoke attributes and methods in it when an object is created.
    def __init__(self,value):
        self.value = value; # Assigning value to the Node.
        self.next = None; # Setting next address as None - Default


# Creating class for Linked List

class LinkedList:
    # Creating initializer function to create a link with HEAD and TAIL to NONE
    def __init__(self):
        self.head = None;
        self.tail = None;
    # Creating a add_link function to insert a node into Linked List
    def add_link(self,value):
        # Creating object to call Node class
        new_node = Node(value);
        # If this is the first node then HEAD and TAIL points to the same node.
        if self.head == None:
            self.head = new_node;
            self.tail = new_node;
        else:
        # This will add the node to the end of the linked list
            self.tail.next = new_node;
            self.tail = new_node;

ll = LinkedList(); # Object creation of the linked list clas. Object is ll
ll.add_link(10); # Adding a node with value 10
print(ll.head.value);
print(ll.head); # Prints address of the HEAD
print(ll.tail); # Prints address of the TAIL.
print(ll); # Prints address of the Node
