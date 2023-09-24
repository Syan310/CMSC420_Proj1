import json
from typing import List

# DO NOT MODIFY THIS CLASS!
class Node():
    def  __init__(self,
                  key        = None,
                  keycount   = None,
                  leftchild  = None,
                  rightchild = None):
        self.key        = key
        self.keycount   = keycount
        self.leftchild  = leftchild
        self.rightchild = rightchild

# DO NOT MODIFY THIS FUNCTION!
# For the tree rooted at root, dump the tree to stringified JSON object and return.
# NOTE: in future projects you'll need to write the dump code yourself,
# but here it's given to you.
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "key": node.key,
            "keycount": node.keycount,
            "leftchild": (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "rightchild": (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr,indent = 2)

#---------------------------------------------------------------------------------------------------

# For the tree rooted at root and the key given:
# If the key is not in the tree, insert it with a keycount of 1.
# If the key is in the tree, increment its keycount.
def insert(root: Node, key: int) -> Node:
    if not root :
        return Node(key = key, keycount = 1)
    
    
    if key == root.key:
        root.keycount += 1
        
    elif key < root.key:
        root.leftchild = insert(root.leftchild, key)
        
    else:
        root.rightchild = insert(root.rightchild, key)
        
    return root




def minValue(node: Node) -> Node:
        curr = node
        while curr.leftchild:
            curr = curr.leftchild
        return curr

# For the tree rooted at root and the key given:
# If the key is not in the tree, do nothing.
# If the key is in the tree, decrement its key count. If they keycount goes to 0, remove the key.
# When replacement is necessary use the inorder successor.


def delete(root: Node, key: int) -> Node:
    if not root:
        return None

    if key == root.key:
        root.keycount -= 1
        if root.keycount <= 0:
            # If node with two children, get the inorder successor
            if root.leftchild and root.rightchild:
                successor = root.rightchild
                while successor.leftchild:
                    successor = successor.leftchild
                root.key, root.keycount = successor.key, successor.keycount
                root.rightchild = delete(root.rightchild, successor.key)
            else:
                root = root.leftchild or root.rightchild
    elif key < root.key:
        root.leftchild = delete(root.leftchild, key)
    else:
        root.rightchild = delete(root.rightchild, key)
    return root




    
# For the tree rooted at root and the key given:
# Calculate the list of keys on the path from the root towards the search key.
# The key is not guaranteed to be in the tree.
# Return the json.dumps of the list with indent=2.
def search(root: Node, search_key: int) -> str:
    path = []
    current = root
    while current:
        path.append(current.key)
        if search_key == current.key:
            break
        elif search_key < current.key:
            current = current.leftchild
        else:
            current = current.rightchild
    return json.dumps(path, indent=2)

# For the tree rooted at root, find the preorder traversal.
# Return the json.dumps of the list with indent=2.
def _preorder(node: Node, result: List[int]):
    if node:
        result.append(node.key)
        _preorder(node.leftchild, result)
        _preorder(node.rightchild, result)

def preorder(root: Node) -> str:
    result = []
    _preorder(root, result)
    return json.dumps(result, indent=2)



# For the tree rooted at root, find the inorder traversal.
# Return the json.dumps of the list with indent=2.

def inorder(root: Node) -> str:
    result = []
    def inorder_h(node):
        if not node:
            return
        inorder_h(node.leftchild)
        result.append(node.key)
        inorder_h(node.rightchild)
    inorder_h(root)
    return json.dumps(result, indent=2)



# For the tree rooted at root, find the postorder traversal.
# Return the json.dumps of the list with indent=2.
def postorder(root: Node) -> str:
    result = []
    def postorder_h(node):
        if not node:
            return
        postorder_h(node.leftchild)
        postorder_h(node.rightchild)
        result.append(node.key)
    postorder_h(root)
    return json.dumps(result, indent=2)


# For the tree rooted at root, find the BFT traversal (go left-to-right).
# Return the json.dumps of the list with indent=2.
def bft(root: Node) -> str:
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.key)
            queue.append(current.leftchild)
            queue.append(current.rightchild)
    return json.dumps(result, indent=2)
