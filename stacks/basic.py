class Stack:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def printALL(self):
        print(self.items)

if __name__=="__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print("TOS: ",s.peek())
    print("ALL: ",s.printALL())
    print("reverse: ")
    while (not s.is_empty()):
        print(s.pop())