# Creating a linked list and printing elements in it using __str__ method
# Method __str__ should return string, not print.
# __str__ method is to return human readable or information or string representation of an object.
class Node:
    def __init__(self,value):
        self.value = value;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;

    # Printing the values
    def __str__(self):
        temp_node = self.head;
        result = '';
        while temp_node is not None:
            result += str(temp_node.value);
            if temp_node.next is not None:
                result += '->';
            temp_node = temp_node.next;
        return result;

    def add_node(self,value):
        new_node = Node(value);
        if self.head == None:
            self.head = new_node;
            self.tail = new_node;
        else:
            # Insert at the end
            self.tail.next = new_node;
            self.tail = new_node;

ll = LinkedList();
ll.add_node(10);
ll.add_node(20);
ll.add_node(30);
print(ll);
