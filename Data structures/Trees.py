from collections import deque

class Node:
    def __init__(self,data=None):
        self.data = data
        self.right_child = None 
        self.left_child = None
        
    # DFS
        
    def inorder(self,root_node):
        current  = root_node
        if current is None:return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)
        
    def preorder(self, root_node):
        current = root_node
        if current is None:return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)
        
    def postorder(self ,root_node):
        current = root_node
        if current is None:return
        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)
    
class Tree:
    def breadth_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
                
        return list_of_nodes
    