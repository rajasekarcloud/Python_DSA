# Insertion at the Beginning of a Singly Linked List
# Write a function to insert a new element at the beginning of a singly linked list. LinkedList and Node class are already provided.
# Note: We already have linked list.
# So, when we insert at the beginning the existing 1st node becomes 2nd node.
# Which means current self.head become new_node next node.
# Then new_node becomes self.head (HEAD)
class Node:
    def __init__(self, value):
        self.value = value;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;

    def prepend(self, value):
        new_node = Node(value);
        new_node.next = self.head;
        self.head = new_node;
        self.length +=1;

ll = LinkedList();
ll.prepend(10);
ll.prepend(20);
print(ll.head.value);
