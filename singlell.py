class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.temp=self.head

        else:
            self.head.next=newnode
            self.temp=newnode


    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.tail.data,'\t')
            self.temp = self.temp.next
        print()

            
obj=SLL()
while True:
    print("1.create 2.display 3.exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        data=int(input("Enter the data:"))
        obj.create(data)
    elif choice==2:
        obj.display()
    elif choice==3:
        break
    else:
        print("Enter the valid number")
