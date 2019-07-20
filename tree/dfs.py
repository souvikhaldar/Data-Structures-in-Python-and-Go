class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self,data):
        self.root = Node(data)

    # root --> left --> right
    def pre_order(self,start):
        if start:
            print(start.data,end=" ")
            self.pre_order(start.left)
            self.pre_order(start.right)
        return         

    # left--> right --> root
    def post_order(self,start):
        if start:
            self.post_order(start.left)
            self.post_order(start.right)
            print(start.data,end= " ")
        return

    # left --> root --> right
    def in_order(self,start):
        if start:
            self.in_order(start.left)
            print(start.data,end=" ")
            self.in_order(start.right)
        return
if __name__=="__main__":
    tree = Tree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print("Preorder:")
    tree.pre_order(tree.root)
    print()
    print("Inorder:")
    tree.in_order(tree.root)
    print()
    print("Postorder:")
    tree.post_order(tree.root)
    print()

