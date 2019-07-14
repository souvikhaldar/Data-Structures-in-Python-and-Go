class Node:
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data

class DLL:
    def __init__(self):
        self.head = None

    def insertAtBeg(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            new_node.next.prev = new_node
            self.head = new_node
    # insert after the position which contains the data `prev_data`
    def insertAtPos(self,data,prev_data):
        new_node = Node(data)
        temp = self.head
        while (temp.data != prev_data):
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        new_node.next.prev = new_node


    def printDLL(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    dll = DLL()
    dll.insertAtBeg(1)
    dll.insertAtBeg(2)
    dll.printDLL()
    dll.insertAtBeg(3)
    dll.insertAtPos(4,2)
    dll.printDLL()
