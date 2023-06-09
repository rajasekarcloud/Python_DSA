# Creating a linked list and printing elements in it using __str__ method
# Method __str__ should return string, not print.
# __str__ method is to return human readable or information or string representation of an object.
# Insert at the beginning and end of the linked list
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

    def add_end_node(self,value):
        new_node = Node(value);
        if self.head == None:
            self.head = new_node;
            self.tail = new_node;
        else:
            # Insert at the end
            self.tail.next = new_node;
            self.tail = new_node;

    def add_begin_node(self,value):
        new_node = Node(value);
        if self.head is None:
            self.head = new_node;
            self.tail = new_node;
        else:
         # Current HEAD node will be next node of the new node
            new_node.next = self.head;
            self.head = new_node;
    def middle_insert(self,index,value):
        new_node = Node(value);
        temp_node = self.head;
        for _ in range(index - 1):
            temp_node = temp_node.next;
        new_node.next = temp_node.next;
        temp_node.next = new_node;

ll = LinkedList();
ll.add_end_node(10);
ll.add_end_node(20);
ll.add_end_node(30);
print(ll);
ll.add_begin_node(40);
ll.add_begin_node(50);
print(ll);
ll.middle_insert(2,100);
print(ll);
