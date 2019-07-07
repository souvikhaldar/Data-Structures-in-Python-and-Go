class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert a node at the begining of the linked list
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self,key):
        flag = 0
        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        while (temp.next):
            if temp.next.data == key:
                temp.next = temp.next.next
                flag = 1
                break
            temp = temp.next
        
        if flag == 0:
            print("Key not found")
    def printLL(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.delete(5)
    ll.printLL()

            

