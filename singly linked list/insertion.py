class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    # Inserting a node at the begining of the linked list
    def insertAtBeg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insert after a given node
    def insertAfter(self,prev_node,data):
        new_node = Node(data)
        if prev_node is None:
            print("Provided node is invalid")
        
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self,data):
        new_node = Node(data)
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def printLL(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBeg(2)
    ll.insertAtEnd(4)
    ll.insertAtBeg(1)
    ll.insertAfter(ll.head,5)
    ll.insertAfter(ll.head.next,6)
    ll.printLL()


        


