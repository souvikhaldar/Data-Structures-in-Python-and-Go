package main

import "fmt"

type node struct {
	data  int
	left  *node
	right *node
}

func newNode(val int) *node {
	return &node{
		data:  val,
		left:  nil,
		right: nil,
	}
}

type BST struct {
	root *node
}

func newBST() *BST {
	return &BST{
		root: nil,
	}
}

func (b *BST) insert(val int) {
	fmt.Println("Inserting: ", val)
	new := newNode(val)
	if b.root == nil {
		b.root = new
		return
	}
	temp := b.root
	for {
		if val > temp.data {
			if temp.right == nil {
				temp.right = new
				break
			} else {
				temp = temp.right
			}
		} else {
			if temp.left == nil {
				temp.left = new
				break
			} else {
				temp = temp.left
			}
		}
	}
}

func (b *BST) getParentNode(child *node) *node {
	temp := b.root
	for temp != nil {
		if temp.left == child || temp.right == child {
			return temp
		}
		if child.data > temp.data {
			temp = temp.right
		} else {
			temp = temp.left
		}
	}
	return nil
}

func (b *BST) delete(val int) {
	temp := b.root
	for temp != nil {
		if val == temp.data {
			fmt.Printf("%d has been found!\n", val)
			// now three situations may arise
			// 1. The node is leaf node
			if temp.right == nil && temp.left == nil {
				fmt.Println("The node is leaf node")
				if val == b.root.data {
					fmt.Println("About to delete root node")
					b.root = nil
					return
				}
				parent := b.getParentNode(temp)
				if parent == nil {
					fmt.Println("Something weird has happend, no parent")
					return
				}
				if parent.left == temp {
					parent.left = nil
				} else if parent.right == temp {
					parent.right = nil
				} else {
					fmt.Println("Something weird has happened. Parent: ", parent.data)
				}
				fmt.Println("Successfully deleted")
				return
			}
			// 2. The node has has one child
			if (temp.right == nil && temp.left != nil) || (temp.right != nil && temp.left == nil) {
				fmt.Println("The node has one child")
				if val == b.root.data {
					fmt.Println("About to delete root node")
					if b.root.right != nil {
						b.root = b.root.right
					} else {
						b.root = b.root.left
					}
					return
				}
				parent := b.getParentNode(temp)
				if parent.left.data == val {
					if parent.left.left != nil {
						parent.left = parent.left.left
					} else {
						parent.left = parent.left.right
					}
				} else {
					if parent.right.left != nil {
						parent.right = parent.right.left
					} else {
						parent.right = parent.right.right
					}
				}
				fmt.Println("Successfully deleted")
				return
			}
			// 3. The node has both children
			if temp.right != nil && temp.left != nil {
				fmt.Println("The node has both children")
				// Now we can go about it in two ways:
				// 1. Swap this node with the maximum value
				// node in the left sub-tree (i.e predecessor,
				// rightmost node in left sub-tree)
				// then delete this node (which would be a leaf node)
				// 2. Swap this node with the minimum value
				// node from the right sub-tree (i.e successor,
				// leftmost node in the right sub-tree) then
				// delete this node which might be having single
				// or both child.
				// Since in case (1) we end up having a leaf node
				// to delete, which is easier, hence we'll follow
				// (1) option.

				// get the predecessor
				predecessor := temp.left
				for predecessor.right != nil {
					predecessor = predecessor.right
				}
				parentOfPredecessor := b.getParentNode(predecessor)
				// swap or put the value of predecessor to temp
				temp.data = predecessor.data
				if parentOfPredecessor.right == predecessor {
					parentOfPredecessor.right = nil
				} else {
					parentOfPredecessor.left = nil
				}
				fmt.Println("Successfully deleted")
				return

			}
		} else if val > temp.data {
			temp = temp.right
		} else {
			temp = temp.left
		}
	}
	fmt.Println("Node not found")
	return
}

func inOrder(n *node) {
	if n == nil {
		return
	}
	inOrder(n.left)
	fmt.Println(n.data)
	inOrder(n.right)
}
func main() {
	// create a new BST
	bst := newBST()
	bst.insert(2)
	bst.insert(6)
	bst.insert(9)
	bst.insert(1)
	fmt.Println("Inorder traversal: ")
	inOrder(bst.root)
	fmt.Println("Delete node with value 6")
	bst.delete(6)
	fmt.Println("Inorder traversal: ")
	inOrder(bst.root)
}
