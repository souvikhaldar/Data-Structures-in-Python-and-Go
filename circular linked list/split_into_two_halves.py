# Split a circular linked list into two halves
# my solution for https://www.geeksforgeeks.org/split-a-circular-linked-list-into-two-halves/

class Node:
    def __init__(self,data):
        self.data = data
class CLL:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        self.head = new_node

    def app(self,data):
        new_node = Node(data)
        if self.head is not None:
            temp = self.head
            while True:
                if temp.next == self.head:
                    break
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        else:
            new_node.next = new_node
            self.head = new_node
            


    def split(self):
        size = 0
        if self.head is not None:
            temp = self.head
            while temp.next != self.head:
                size +=1
                temp = temp.next
            f_size = size +1
        
        mid = f_size//2

        first_cll = CLL()
        temp = self.head
        for i in range(mid):
            first_cll.app(temp.data)
            temp = temp.next

        second_cll = CLL()
        

        while True:
            second_cll.app(temp.data)
            if temp.next == self.head:
                break 
            temp = temp.next
        return first_cll,second_cll

            



    def printCLL(self):
        if self.head is not None:
            temp = self.head
            while True:
                print(temp.data)
                if temp.next == self.head:
                    break
                temp = temp.next
        else:
            print("Empty CLL")

if __name__ == "__main__":
    cll = CLL()
    cll.printCLL()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)
    cll.insert(4)
    cll.insert(5)
    cll.printCLL()
    cll.split()
    print("splitting")
    a = cll.split()
    print("first:")
    a[0].printCLL()
    print("second:")
    a[1].printCLL()



