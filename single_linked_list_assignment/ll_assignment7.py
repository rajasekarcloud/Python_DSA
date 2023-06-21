# Reverse a Singly Linked List
# Write a function to reverse a singly linked list. The function should return a new linked list that is the reverse of the original list.
#
# Example:
#
# Original singly linked list:   1 -> 2 -> 3 -> 4 -> 5
#
# Reversed singly linked list:  5 -> 4 -> 3 -> 2 -> 1
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def reverse(self):
        # It keeps track of the previous node during traversal.
        prev_node = None
        # Initializes current_node with the head of the linked list. The reverse operation starts from here.
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next # Save the next node to tmp before breaking the link
            current_node.next = prev_node # Break the link
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

ll = LinkedList();
ll.append(1);
ll.append(2);
ll.append(3);
ll.append(4);
ll.append(5);
print(ll);
ll.reverse();
print(ll);
