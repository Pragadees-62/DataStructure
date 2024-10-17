'''def check(s):
    stack=[]
    for char in s:
        if char in ['{','[','(',]:
            stack.append(char)
        else:
            if not stack:
                return False
            val=stack.pop()
            if val=='(':
                if char!=')':
                    return False
            if val=='{':
                if char!='}':
                    return False
            if val=='[':
                if char!=']':
                    return False
    return not stack
s=input()
if (check(s)):
    print("BALANCED")
else:
    print("UNBALANCED")'''
def check(s):
    stack = []
    for char in s:
        if char in ['{', '[', '(']:  
            stack.append(char)
        elif char in ['}', ']', ')']:  
            if not stack:
                return False
            val = stack.pop()
            if char == ')' and val != '(':
                return False
            if char == '}' and val != '{':
                return False
            if char == ']' and val != '[':
                return False
    
    
    return not stack


s = input("Enter the string to check: ")


if check(s):
    print("BALANCED")
else:
    print("UNBALANCED")

