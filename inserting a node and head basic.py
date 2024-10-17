class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_start(self,data):
        newnode=Node(data)
        newnode.next= self.head
        self.head=newnode

    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
        print("NULL")


LD=SinglyLinkedList()
LD.insert_at_start(10098)
LD.insert_at_start(400)
LD.insert_at_start(299)
LD.insert_at_start(87)
LD.insert_at_start(34)
LD.insert_at_start(12)
LD.insert_at_start(7)

LD.display ()
