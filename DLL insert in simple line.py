class node:
    def _init_(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def _init_(self):
        self.head=None
        self.tail=None
    def create(self,data):
        if(self.head==None):
            self.head=node(data)
            self.tail=self.head
        else:
            newnode=node(data)
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
    def insertbeg(self,data):
        newnode=node(data)
        if(self.head!=None):
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
    def insertend(self,data):
        newnode=node(data)
        if(self.tail!=None):
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
    def insertmid(self,data,pos):
        newnode=node(data)
        temp=self.head
        i=1
        while(i<pos):
            temp=temp.next
            i=i+1
        newnode.next=temp.next
        newnode.prev=temp
        temp.next=newnode
        newnode.next.prev=temp






    
    def display(self):
        temp=self.head
        while(temp!=None):
            print(id(temp.prev),temp.data,id(temp.next))
            temp=temp.next

obj=dll()
n=int(input("Enter The Number:"))
for i in range(n):
    m=int(input("Enter The Element:"))
    obj.create(m)
obj.display()
s=int(input("Insert At Begin:"))
obj.insertbeg(s)
obj.display()
b=int(input("Insert At End:"))
obj.insertend(b)
obj.display()
c=int(input("Insert At Middle:"))
pos=int(input())
obj.insertmid(c,pos)
obj.display()
