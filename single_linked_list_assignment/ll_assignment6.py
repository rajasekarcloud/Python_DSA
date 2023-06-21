# Deletion from a Singly Linked List
# Write a function to delete a node from a singly linked list.
# The function should take the index(starting from 0) of the node to be deleted as a parameter.

def remove(self, index):
    # check if the index is 0 - empty or index greater than the length of the list
    if index < 0 or index >= self.length:
        return None;
    # If the node to be removed is HEAD - index == 0
    # This conditional checks whether the provided index is 0, meaning that the head of the list should be removed.
    elif index == 0:
        # If the head is to be removed, the method saves a reference to it in the popped_node variable.
        popped_node = self.head;
        # This conditional checks whether the list only contains one node.
        if self.length == 1:
            self.head = None;
            self.tail = None;
        else:
            # It removes the head by setting the head of the list to the next node in the list.
            self.head = self.head.next;
        popped_node.next = None;
        self.length -= 1;
        return popped_node;
    else:
        temp = self.head;
        for _ in range(index - 1):
            temp = temp.next;
        popped_node = temp.next;

        # If node to be removed is the tail node
        if popped_node.next is None:
            self.tail = temp;

        temp.next = temp.next.next;
        popped_node.next = None;
        self.length -= 1;
        return popped_node;
