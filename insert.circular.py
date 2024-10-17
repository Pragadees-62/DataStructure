class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node  
        return new_node
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = new_node  
        new_node.next = head  
        return new_node  

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node  
        return new_node
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = new_node  
        new_node.next = head  
        return head  

def insert_in_middle(head, data, after_value):
    if head is None:
        return None 

    new_node = Node(data)
    current = head

    while True:
        if current.data == after_value:
            new_node.next = current.next
            current.next = new_node
            return head
        current = current.next
        if current == head:  
            break

    print("Value not found in the list.")
    return head

def print_list(head):
    if head is None:
        return
    current = head
    while True:
        print(current.data, end=" -> ")
        current = current.next
        if current == head:
            break
    print("(back to head)")


if __name__ == "__main__":
    head = None

    
    head = insert_at_beginning(head, 10)
    head = insert_at_beginning(head, 20)

   
    head = insert_at_end(head, 30)

    
    head = insert_in_middle(head, 25, 20)

     print_list(head)
