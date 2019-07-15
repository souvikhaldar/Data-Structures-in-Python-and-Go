class Node:
    def __init__(self,data):
        self.data = data
        self.prev =None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def insertAtBeg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is None:
            new_node.prev = None        
        else:    
            new_node.prev = None
            new_node.next.prev = new_node
            
        self.head = new_node

    # to reverse a DLL we just need to swap the next and prev pointers
    def reverse(self):
        prev = None
        curr = self.head
        while (curr):
            fut = curr.next
            curr.prev = curr.next
            curr.next = prev
            prev = curr 
            curr = fut

        self.head = prev 
            



    def printDLL(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next 

if __name__ == "__main__":
    dll = DLL()
    dll.insertAtBeg(3)
    dll.insertAtBeg(2)
    
    dll.printDLL()
    print("--reversing--")
    dll.reverse()
    dll.printDLL()