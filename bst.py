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
    if key == root.key:
        root.keycount += 1
    elif key < root.key:
        root.leftchild = insert(root.leftchild, key)
    else:
        root.rightchild = insert(root.rightchild, key)
    return root

# Helper function to find the minimum value node
def _find_min(node: Node) -> Node:
    current = node
    while current.leftchild:
        current = current.leftchild
    return current

# Delete function
def delete(root: Node, key: int) -> Node:
    if not root:
        return root
    if key < root.key:
        root.leftchild = delete(root.leftchild, key)
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    else:
        root.keycount -= 1
        if root.keycount == 0:
            if not root.leftchild:
                return root.rightchild
            elif not root.rightchild:
                return root.leftchild
            temp = _find_min(root.rightchild)
            root.key = temp.key
            root.keycount = temp.keycount
            root.rightchild = delete(root.rightchild, temp.key)
    return root

# Search function
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

# Preorder function
def _preorder(node: Node, result: List[int]):
    if node:
        result.append(node.key)
        _preorder(node.leftchild, result)
        _preorder(node.rightchild, result)

def preorder(root: Node) -> str:
    result = []
    _preorder(root, result)
    return json.dumps(result, indent=2)

# Inorder function
def _inorder(node: Node, result: List[int]):
    if node:
        _inorder(node.leftchild, result)
        result.append(node.key)
        _inorder(node.rightchild, result)

def inorder(root: Node) -> str:
    result = []
    _inorder(root, result)
    return json.dumps(result, indent=2)

# Postorder function
def _postorder(node: Node, result: List[int]):
    if node:
        _postorder(node.leftchild, result)
        _postorder(node.rightchild, result)
        result.append(node.key)

def postorder(root: Node) -> str:
    result = []
    _postorder(root, result)
    return json.dumps(result, indent=2)

# BFT function
def bft(root: Node) -> str:
    if not root:
        return json.dumps([], indent=2)
    queue, result = [root], []
    while queue:
        current = queue.pop(0)
        result.append(current.key)
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)
    return json.dumps(result, indent=2)
