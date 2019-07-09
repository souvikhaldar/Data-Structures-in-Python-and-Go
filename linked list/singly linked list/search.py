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


    def IterativeSearch(self,key):
        temp = self.head

        while (temp):
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def RecursiveSearch(self,list,key):
        if (not list):
            return False
        if list.data == key:
            return True
        return self.RecursiveSearch(list.next,key)

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.push(2)
    ll.push(4)
    ll.push(6)
    print(ll.RecursiveSearch(ll.head,4))
    print(ll.IterativeSearch(5))
    ll.printList()


