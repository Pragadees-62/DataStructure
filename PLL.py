class Node:
    def __init__(self,coef,exp):
        self.coef=coef
        self.exp=exp
        self.next=None

class PLL:
    def __init__(self):
        self.head=None
    def create(self,coef,exp):
        newnode=Node(coef,exp)
        if(self.head==None):
            self.head=newnode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode

    def add(self,val):
        result=PLL()
        sum=0
        p1=self.head
        p2.val.head
        while p1 and p2:
            if (p1.exp==p2.exp):
                sum=p1.coef+p2.coef
                if sum!=0:
                    res.create(sum,p1.exp)
                    p1=p1.next
                    p2=p2.next
                
            elif p1.exp > p2.exp:
                res.create(p1.coef,p1.exp)
                p1=p1.next
            else:
                res.create(p2.coeff,p2.exp)
                p2=p2.next
        while p1:
            res.create(p1.coef,p1.exp)
            p1=p1.next
        while p2:
            res.create(p2.coef,p2.exp)
            p2=p2.next
        

    def display(self):
        temp=self.head
        poly=[]
        while temp!=None:
            poly.append(f"{temp.coef}X^{temp.exp}")
            temp=temp.next
        print("+".join(poly))


obj=PLL()
n=int(input())
for i in range(n):
    a,b=input().split()
    obj.create(a,b)

obj.display()
obj1=PLL()
s=int(input())
for i in range (s):
    

                    
