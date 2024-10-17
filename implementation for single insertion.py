class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None

    def add(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
    
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")
LL=LinkedLists()
LL.add(122)
LL.add(150)
LL.add(240)


LL.print_list()
    
