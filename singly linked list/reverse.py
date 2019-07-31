class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        past = None
        present = self.head
        while(present is not None):
            future = present.next
            present.next = past
            past = present
            present = future
        self.head = past
        
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(3)
    ll.push(6)
    ll.push(9)
    ll.printList()
    print("--reversing--")
    ll.reverse()
    ll.printList()