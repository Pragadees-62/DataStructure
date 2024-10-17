stack=[]
def push():
    m=int(input())
    stack.append(m)
    print(stack)
def pop():
    e=stack.pop()
    print(e)
    print(stack)
def peek():
    print(stack[-1])
n=int(input())
while True:
    c=int(input())
if c==1:
    push()
elif c==2:
    pop()
