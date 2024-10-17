class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.temp=self.head
        else:
            self.temp.next=newnode
            newnode.prev=self.temp
            self.temp=self.temp.next
    def display(self):
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        while self.temp !=self.head:
            print(self.temp.data,end=' ')
            self.temp=self.temp.prev
        print(self.temp.data)
        print()
    def insert_at_front(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    def insert_at_mid(self,data):
        newnode=node(data)
        i=1
        self.temp=self.head
        while i<pos-1:
            self.temp=self.temp.next
            i=i+1
        newnode.next=self.temp.next
        newnode.prev=self.temp
        self.temp.next=newnode
        newnode.next.prev=newnode
    def insert_at_end(self,data):
        newnode=node(data)
        if self.head is None:  
            self.head = newnode
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = newnode
        newnode.prev = temp
        newnode.next = None
obj=DLL()
while(1):
    print("1.create 2.display 3.exit 4.insert_at_front 5.insert_at_mid 6.insert_at_end")
    choice=int(input("enter the choice:"))
    if choice==1:
        data=int(input("enter the data:"))
        obj.create(data)
    elif choice==2:
        obj.display()
    elif choice==3:
        break
    elif choice==4:
        data=int(input("enter the data:"))
        obj.insert_at_front(data)
    elif choice==5:
        data=int(input("enter the data:"))
        pos=int(input("enter the position:"))
        obj.insert_at_mid(data)
    elif choice==6:
        data=int(input("enter the data:"))
        obj.insert_at_end(data)
    else:
        print("Try The Number In Below 6 And Try Again")



"""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def create(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.prev
        print()

    def insert_at_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_mid(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        new_node = Node(data)
        if pos == 1:
            self.insert_at_front(data)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        if temp is None:
            print("Position out of bounds")
            return
        new_node.next = temp.next
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

obj = DLL()
while True:
    print("1. Create 2. Display 3. Exit 4. Insert at front 5. Insert at mid 6. Insert at end")
    choice = int(input("Enter the choice: "))
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
        pos = int(input("Enter the position: "))
        obj.insert_at_mid(data, pos)
    elif choice == 6:
        data = int(input("Enter the data: "))
        obj.insert_at_end(data)
    else:
        print("Try a number between 1 and 6 and try again.")
DLL.insert_at_front(45)
DLL.insert_at_front(9)
DLL.insert_at_end(89)
DLL.insert_at_middle(87)
DLL.insert_at_first(2)

DLL ()"""
