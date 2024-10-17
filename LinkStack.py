class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class stack:
    def _init_(self):
        self.head=None
    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            newnode=node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        last=self.head
        self.head=self.head.next
        print(last.data)
    def peek(self):
        print(self.head.data)
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,id(temp.next))
            temp=temp.next

o=stack()
n=int(input())
for i in range(n):
    c= list(input().split())
    if c[0]=="push":
        o.push(int(c[1]))
    elif c[0]=="pop":
        o.pop()
    elif c[0]=="peek":
        o.peek()
    elif c[0]=="isEmpty":
        print(o.is_empty())
