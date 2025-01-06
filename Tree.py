class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BST():
    def __init__(self):
        self.root=None
        self.length=0
    def insert(self,value):
        node=Node(value)
        if self.root==None:
            self.root=node
        current=self.root
        while (current.left!=node) and (current.right!=node)  :
            if node.value>current.value:
                if current.right==None:
                    current.right=node
                current=current.right
            elif node.value<current.value:
                if current.left==None:
                    current.left=node
                current=current.left
            self.length+=1
            return
    def search(self,value):
        current=self.root
        if self.root==None:
            print("Empty Tree")
        while current :
            if value>current.value:
                
                current=current.right
            elif value<current.value:
               
                current=current.left
            else:
                return "Found"
        return 'Not Found'
    def DFS_inorder(self):
        return inorder_transversal(self.root,[])
    def DFS_preorder(self):
        return preorder_transversal(self.root,[])
    def DFS_postorder(self):
        return postorder_transversal(self.root,[])
def inorder_transversal(node,DFS_list):
    if node.left:
        inorder_transversal(node.left,DFS_list)
    DFS_list.append(node.value)
    if node.right:
       inorder_transversal(node.right,DFS_list)
    return DFS_list
    
def preorder_transversal(node,DFS_list):
    DFS_list.append(node.value)
    if node.left:
        preorder_transversal(node.left,DFS_list)
    
    if node.right:
       preorder_transversal(node.right,DFS_list)
    return DFS_list
def postorder_transversal(node,DFS_list):
    
    if node.left:
        postorder_transversal(node.left,DFS_list)
    
    if node.right:
       postorder_transversal(node.right,DFS_list)
    DFS_list.append(node.value)
    return DFS_list
        
bst=BST()
bst.insert(5)
bst.insert(4)
bst.insert(6)
print(bst.search(6))
print(bst.search(7))
print(bst.DFS_inorder())
print(bst.DFS_preorder())
print(bst.DFS_postorder())
        
              
            
        