#tree
class Tree:
    def __init__(self,key,left=None,right=None):
        self.val=key
        self.left=left
        self.right=right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.right=Tree(4)
root.left.left=Tree(5)
print(inorder(root))