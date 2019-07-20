class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = self.rear = None

    # check if queue is empty
    def isEmpty(self):
        return self.front == None
    # insert new node to the rear
    def enqueue(self,data):
        temp = Node(data)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # remove the element from the begining
    def dequeue(self):
        if self.isEmpty():
            return
        beg = self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return beg.data

    def printQ(self):
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next
        

if __name__=="__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()
    q.printQ()
