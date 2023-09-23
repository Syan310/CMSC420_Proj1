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


def minValueNode(node: Node) -> Node:
    current = node
    while current.leftchild:
        current = current.leftchild
    return current

# For the tree rooted at root and the key given:
# If the key is not in the tree, do nothing.
# If the key is in the tree, decrement its key count. If they keycount goes to 0, remove the key.
# When replacement is necessary use the inorder successor.
def delete(root: Node, key: int) -> Node:
    if not root:
        return root
    
    if key < root.key:
        root.leftchild = delete(root.leftchild, key)
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    else:
        if root.keycount > 1:
            root.keycount -= 1
            return root
        else:
            if not root.leftchild:
                temp = root.rightchild
                root = None
                return temp
            elif not root.rightchild:
                temp = root.leftchild
                root = None
                return temp

            temp = minValueNode(root.rightchild)
            root.key = temp.key
            root.keycount = temp.keycount
            root.rightchild = delete(root.rightchild, temp.key)

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


# For the tree rooted at root, find the preorder traversal.
# Return the json.dumps of the list with indent=2.
def preorder(root: Node) -> str:
        result = []

        def helper(node: Node):
            if not node:
                return
            result.append(node.key)
            helper(node.leftchild)
            helper(node.rightchild)

        helper(root)
        return json.dumps(result, indent=2)

# For the tree rooted at root, find the inorder traversal.
# Return the json.dumps of the list with indent=2.
def inorder(root: Node) -> str:
    result = []

    def helper(node: Node):
        if not node:
            return
        helper(node.leftchild)
        result.append(node.key)
        helper(node.rightchild)

    helper(root)
    return json.dumps(result, indent=2)


# For the tree rooted at root, find the postorder traversal.
# Return the json.dumps of the list with indent=2.
def postorder(root: Node) -> str:
    result = []

    def helper(node: Node):
        if not node:
            return
        helper(node.leftchild)
        helper(node.rightchild)
        result.append(node.key)

    helper(root)
    return json.dumps(result, indent=2)

# For the tree rooted at root, find the BFT traversal (go left-to-right).
# Return the json.dumps of the list with indent=2.
def bft(root: Node) -> str:
    result = []
    if not root:
        return json.dumps(result, indent=2)

    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.key)
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)

    return json.dumps(result, indent=2)
