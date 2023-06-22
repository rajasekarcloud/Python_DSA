# Middle of a Singly Linked List
# Write a function to find and return the middle node of a singly linked list.
# If the list has an even number of nodes, return the second of the two middle nodes.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        # slow = self.head - This line initializes the slow pointer at the head of the linked list.
        # This pointer will move one node at a time through the list.
        slow = self.head
        # fast = self.head - This line initializes the fast pointer also at the head of the linked list.
        # This pointer will move two nodes at a time through the list.
        fast = self.head
        #  if not self.head: - This line checks if the head of the linked list is None. If it is, that means the list is empty and there is no middle node to find.

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # return slow - After the while loop, the slow pointer will be at the middle of the linked list. This line returns the slow node, which is the middle node of the list.
        
        return slow;

ll = LinkedList();
ll.append(10);
ll.append(20);
ll.append(30);
ll.find_middle();
