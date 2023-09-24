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
    if root is None:
        return Node(key = key, keycount = 1)
    
    
    if key == root.key:
        root.keycount += 1
        
    elif key < root.key:
        root.leftchild = insert(root.leftchild, key)
        
    else:
        root.rightchild = insert(root.rightchild, key)
        
    return root



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
    list = []
    curr = root
   
    while curr:
        list.append(curr.key)
        
        if curr.key == search_key:
            break
        elif curr.key > search_key:
            curr = curr.leftchild
        elif curr.key < search_key:
            curr = curr.rightchild
            
    return (json.dumps(list, indent=2))


def _traversal(root: Node, order="in"):
    result = []
    if not root:
        return result

    if order == "pre":
        result.append(root.key)
    result.extend(_traversal(root.leftchild, order))
    if order == "in":
        result.append(root.key)
    result.extend(_traversal(root.rightchild, order))
    if order == "post":
        result.append(root.key)
    return result

def preorder(root: Node) -> str:
    return json.dumps(_traversal(root, "pre"), indent=2)

def inorder(root: Node) -> str:
    return json.dumps(_traversal(root, "in"), indent=2)

def postorder(root: Node) -> str:
    return json.dumps(_traversal(root, "post"), indent=2)

def bft(root: Node) -> str:
    if not root:
        return json.dumps([], indent=2)
    result, queue = [], [root]
    while queue:
        current = queue.pop(0)
        result.append(current.key)
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)
    return json.dumps(result, indent=2)
