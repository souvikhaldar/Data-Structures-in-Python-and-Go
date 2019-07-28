''' 
You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

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
  
def revsum(node1,node2,ll3,carry):
 if node1 is None or node2 is None:
  return ll3
 return revsum(node1.next,node2.next,ll3,carry)
 sumi = node1.data + node2.data + carry
 print("inter sum ",sumi)
 if sumi >= 10:
  ll3.addEnd(sumi%10)
  carry = sumi // 10
 else:
  ll3.addEnd(sumi)
  carry = 0
 print("inter list:")
 ll3.rprint(ll3.head)
if __name__== "__main__":
 ll = LL()
 ll2 = LL()
 ll.addEnd(2)
 ll.addEnd(4)
 ll.addEnd(3)
 ll2.addEnd(5)
 ll2.addEnd(6)
 ll2.addEnd(4)
 #ll.fprint(ll.head)
 print("reverse sum:")
 ll3 = LL()
 f = revsum(ll.head,ll2.head,ll3,0)
 f.rprint(f.head)
 #print("reverse print")
 #ll.rprint(ll.head)