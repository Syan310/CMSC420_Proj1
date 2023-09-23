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
    if not root:
        return Node(key=key, keycount=1)

    # Key already exists in tree
    if root.key == key:
        root.keycount += 1

    # Insert in left subtree
    elif key < root.key:
        root.leftchild = insert(root.leftchild, key)

    # Insert in right subtree
    else:
        root.rightchild = insert(root.rightchild, key)

    return root

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
        else:
            if not root.leftchild:
                return root.rightchild
            elif not root.rightchild:
                return root.leftchild
            root.key = get_min(root.rightchild).key
            root.rightchild = delete(root.rightchild, root.key)
    return root

def get_min(node: Node) -> Node:
    while node.leftchild:
        node = node.leftchild
    return node

# For the tree rooted at root and the key given:
# Calculate the list of keys on the path from the root towards the search key.
# The key is not guaranteed to be in the tree.
# Return the json.dumps of the list with indent=2.
def search(root: Node, search_key: int) -> str:
    path = []
    while root:
        path.append(root.key)
        if search_key < root.key:
            root = root.leftchild
        elif search_key > root.key:
            root = root.rightchild
        else:
            break
    return json.dumps(path, indent=2)

# For the tree rooted at root, find the preorder traversal.
# Return the json.dumps of the list with indent=2.
def preorder(root: Node) -> str:
    result = []
    def _preorder(node):
        if node:
            result.append(node.key)
            _preorder(node.leftchild)
            _preorder(node.rightchild)
    _preorder(root)
    return json.dumps(result, indent=2)

# For the tree rooted at root, find the inorder traversal.
# Return the json.dumps of the list with indent=2.
def inorder(root: Node) -> str:
    result = []
    def _inorder(node):
        if node:
            _inorder(node.leftchild)
            result.append(node.key)
            _inorder(node.rightchild)
    _inorder(root)
    return json.dumps(result, indent=2)


# For the tree rooted at root, find the postorder traversal.
# Return the json.dumps of the list with indent=2.
def postorder(root: Node) -> str:
    result = []
    def _postorder(node):
        if node:
            _postorder(node.leftchild)
            _postorder(node.rightchild)
            result.append(node.key)
    _postorder(root)
    return json.dumps(result, indent=2)

# For the tree rooted at root, find the BFT traversal (go left-to-right).
# Return the json.dumps of the list with indent=2.
def bft(root: Node) -> str:
    if not root:
        return json.dumps([], indent=2)

    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)  # pop the first element
        result.append(node.key)
        
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)

    return json.dumps(result, indent=2)
