'''
Implement a class for a stack that supports all the regular functions (push, pop) 
and an additional function of max() which returns the maximum element in the stack
(return None if the stack is empty). Each method should run in constant time.
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None 
    
    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp
    def printStack(self):
        if self.head is None:
            return None
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.printStack()
    print("pop:",s.pop().data)
    s.printStack()
    