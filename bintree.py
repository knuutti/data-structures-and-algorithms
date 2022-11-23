class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
 

class BST:
    def __init__ (self):
        self.root = None

    def search(self, key):
        return self.search_help(self.root, key)

    def search_help(self, node, key):
        if node == None:
            return False
        elif node.key > key:
            return self.search_help(node.left, key)
        elif node.key < key:
            return self.search_help(node.right, key)
        return True

    def insert(self,key):
        self.root = self.insert_help(self.root,key)
        return

    def insert_help(self,node,key):
        if node == None:
            return Node(key)
        if node.key > key:
            node.left = self.insert_help(node.left,key)
        elif node.key < key:
            node.right = self.insert_help(node.right,key)
        return node

    def remove(self,key):
        self.root = self.remove_help(self.root,key)
        return

    def remove_help(self,node,key):
        if node == None:
            return node
        elif node.key > key:
            node.left = self.remove_help(node.left,key)
        elif node.key < key:
            node.right = self.remove_help(node.right,key)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                temp = self.getMax(node.left)
                node.key = temp.key
                node.left = self.remove_help(node.left,node.key)
        return node

    def getMax(self,node):
        if node.right == None:
            return node
        else:
            return self.getMax(node.right)

    def preorder(self):
        self.preorder_help(self.root)
        print()

    def preorder_help(self,node):
        if node == None:
            return
        print(node.key, end=" ")
        self.preorder_help(node.left)
        self.preorder_help(node.right)

    def breadthfirst(self):
        queue = [self.root]
        self.breadthfirst_help(queue)
        print()

    def breadthfirst_help(self,queue):
        node = queue[0]
        queue.pop(0)
        if node != None:
            print(node.key, end=" ")
            queue.append(node.left)
            queue.append(node.right)
        if len(queue) > 0:
            self.breadthfirst_help(queue)






if __name__ == "__main__":
    Tree = BST()
    keys = [5, 3, 8, 7, 9, 6, 4, 1, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6