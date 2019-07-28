class Node:
 def __init__(self,data):
  self.data = data
  self.next = None
  
class LL:
 def __init__(self):
  self.head = None
  
  
 def addEnd(self,data):
  new = Node(data)
  temp = self.head
  if temp is None:
   self.head = new
   return
  while(temp.next):
   temp = temp.next
  temp.next = new
 # recursively print nodes of a linked list
 def fprint(self,node):
  if node is None:
   return
  print(node.data)
  self.fprint(node.next)
  
 def rprint(self,node):
  if node is None:
   return
  self.rprint(node.next)
  print(node.data)
if __name__== "__main__":
 ll = LL()
 ll.addEnd(1)
 ll.addEnd(2)
 ll.addEnd(3)
 ll.fprint(ll.head)
 print("reverse print")
 ll.rprint(ll.head)
  