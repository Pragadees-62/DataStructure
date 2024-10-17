class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.temp = self.head
        else:
            self.temp.next = new_node
            self.temp = new_node

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data,end=' ')
            self.temp = self.temp.next
        print()

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_mid(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_front(data)
            return
        self.temp = self.head
        i = 0
        while self.temp is not None and i < pos - 1:
            self.temp = self.temp.next
            i += 1
        if self.temp is None:
            print("NULL")
            return
        new_node.next = self.temp.next
        self.temp.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.temp = self.head
        while self.temp.next is not None:
            self.temp = self.temp.next
        self.temp.next = new_node

obj = SLL()
while True:
    print("1. Create 2. Display 3. Exit 4. Insert Front 5. Insert Mid 6. Insert End")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        break
    elif choice == 4:
        data = int(input("Enter the data: "))
        obj.insert_at_front(data)
    elif choice == 5:
        data = int(input("Enter the data: "))
        pos = int(input("Enter position: "))
        obj.insert_at_mid(data, pos)
    elif choice == 6:
        data = int(input("Enter the data: "))
        obj.insert_at_end(data)
    else:
        print("Invalid choice")
