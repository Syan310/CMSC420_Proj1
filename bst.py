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

def delete(root: Node, key: int) -> Node:
    if not root:
        return root  # Key not found in the tree
    
    # Traverse to find the node
    if key < root.key:
        root.leftchild = delete(root.leftchild, key)
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    else:  # Node to delete is found
        root.keycount -= 1
        if root.keycount == 0:  # If keycount is 0, delete the node
            # Node with one or no child
            if not root.leftchild:
                temp = root.rightchild
                root = None
                return temp
            elif not root.rightchild:
                temp = root.leftchild
                root = None
                return temp
            
            # Node with two children
            temp = find_min_value_node(root.rightchild)
            root.key = temp.key
            root.keycount = temp.keycount
            root.rightchild = delete(root.rightchild, temp.key)
    
    return root

def find_min_value_node(node):
    current = node
    while current.leftchild is not None:
        current = current.leftchild
    return current

def search(root: Node, search_key: int) -> str:
    path = []
    current = root
    while current:
        path.append(current.key)
        if search_key < current.key:
            current = current.leftchild
        elif search_key > current.key:
            current = current.rightchild
        else:
            break  # Key found
    return json.dumps(path, indent=2)


def preorder(root: Node) -> str:
    result = []
    def _preorder(node):
        if not node:
            return
        result.append(node.key)
        _preorder(node.leftchild)
        _preorder(node.rightchild)
    _preorder(root)
    return json.dumps(result, indent=2)


def inorder(root: Node) -> str:
    result = []
    def _inorder(node):
        if not node:
            return
        _inorder(node.leftchild)
        result.append(node.key)
        _inorder(node.rightchild)
    _inorder(root)
    return json.dumps(result, indent=2)


def postorder(root: Node) -> str:
    result = []
    def _postorder(node):
        if not node:
            return
        _postorder(node.leftchild)
        _postorder(node.rightchild)
        result.append(node.key)
    _postorder(root)
    return json.dumps(result, indent=2)

def bft(root: Node) -> str:
    if not root:
        return json.dumps([], indent=2)
    
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.key)
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)
    
    return json.dumps(result, indent=2)

