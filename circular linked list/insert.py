class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_ll:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
        else:
            temp = self.head    
            while (temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

        self.head = new_node
            


    def printCLL(self):
        if self.head is not None:
            temp = self.head
            while True:
                print(temp.data)
                if (temp.next == self.head):
                    break
                else:
                    temp = temp.next
        else:
            print("Empty CLL")


        

if __name__ == "__main__":
    cll = circular_ll()
    print("1.")
    cll.printCLL()
    cll.insert(2)
    cll.insert(4)
    print("2.")
    cll.printCLL()
    cll.insert(6)
    cll.insert(8)
    print("3.")
    cll.printCLL()
    


            
