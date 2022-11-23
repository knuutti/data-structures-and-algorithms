class AVLNode:
    # Constructor for new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0
    

class AVL:

    # Constructor for new AVL
    def __init__(self):
        self.root = None
        self.is_balanced = True


    # Inserts a new key to the search tree
    def insert(self, key):
        self.root = self.insert_help(self.root, key)

    # Help function for insert
    def insert_help(self, root, key):
        if not root:
            root = AVLNode(key)
            self.is_balanced = False

        elif key < root.key:
            root.left = self.insert_help(root.left, key)
            if not self.is_balanced:                           # Check for possible rotations
                if root.balance >= 0:                       # No Rotations needed, update balance variables
                    self.is_balanced = root.balance == 1
                    root.balance -= 1
                else:                                       # Rotation(s) needed
                    if root.left.balance == -1:
                        root = self.right_rotation(root)    # Single rotation
                    else:
                        root = self.left_right_rotation(root)   # Double rotation
                    self.is_balanced = True

        elif key > root.key:
            root.right = self.insert_help(root.right, key)
            if not self.is_balanced:                           # Check for possible rotations
                if root.balance <= 0:                       # No Rotations needed, update balance variables
                    self.is_balanced = root.balance == -1
                    root.balance += 1
                else:                                       # Rotation(s) needed
                    if root.right.balance == 1:
                        root = self.left_rotation(root)    # Single rotation
                    else:
                        root = self.right_left_rotation(root)   # Double rotation
                    self.is_balanced = True
            
        return root


    # Single rotation: right rotation around root
    def right_rotation(self, root):
        print("SINGLE")
        child = root.left                   # Set variable for child node
        root.left = child.right             # Rotate
        child.right = root
        child.balance = root.balance = 0    # Fix balance variables
        return child


    # Single rotation: left rotation around root 
    def left_rotation(self, root):
        print("SINGLE")
        child = root.right                  
        root.right = child.left             
        child.left = root
        child.balance = root.balance = 0   
        return child


    # Double rotation: left rotation around child node followed by right rotation around root
    def left_right_rotation(self, root):
        print("DOUBLE")
        child = root.left
        grandchild = child.right            # Set variables for child node and grandchild node
        child.right = grandchild.left       # Rotate
        grandchild.left = child
        root.left = grandchild.right
        grandchild.right = root
        root.balance = child.balance = 0    # Fix balance variables
        if grandchild.balance == -1:
            root.balance = 1 
        elif grandchild.balance == 1:
            child.balance = -1
        grandchild.balance = 0
        return grandchild


    # Double rotation: right rotation around child node followed by left rotation around root
    def right_left_rotation(self, root):
        print("DOUBLE")
        child = root.right
        grandchild = child.left            # Set variables for child node and grandchild node
        child.left = grandchild.right       # Rotate
        grandchild.right = child
        root.right = grandchild.left
        grandchild.left = root
        root.balance = child.balance = 0    # Fix balance variables
        if grandchild.balance == 1:
            root.balance = -1 
        elif grandchild.balance == -1:
            child.balance = 1
        grandchild.balance = 0
        return grandchild

    def preorder(self):
        self.preorder_help(self.root)
        print()

    def preorder_help(self,node):
        if node == None:
            return
        print(f"{node.key};{node.balance}", end=" ")
        self.preorder_help(node.left)
        self.preorder_help(node.right)


if __name__ == "__main__":
    Tree = AVL()
    Tree2 = AVL()
    
    for key in [9, 10, 11, 3, 2, 6, 4, 7, 5]:
        Tree.insert(key)

    for key in [5, 10, 11, 3, 2, 4, 6, 7, 9]:
        Tree2.insert(key)

    Tree.preorder()    
    Tree2.preorder()