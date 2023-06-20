# Insertion at the Beginning of a Singly Linked List
# Write a function to insert a new element at the beginning of a singly linked list. LinkedList and Node class are already provided.
class Node:
    def __init__(self, value):
        self.value = value;
        self.next = None;


class LinkedList:
    def __init__(self):
        self.head = None;
        self.length = 0;

    def add_begin(self, value):
        new_node = Node(value);
        if self.head is None:
            self.head = new_node;
            self.tail = None;


ll = LinkedList();
ll.add_begin(10);
print(ll.head.value);
