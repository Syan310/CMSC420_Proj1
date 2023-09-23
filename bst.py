import json
from typing import List
from queue import Queue

class Node():
    def __init__(self, key=None, keycount=None, leftchild=None, rightchild=None):
        self.key = key
        self.keycount = keycount
        self.leftchild = leftchild
        self.rightchild = rightchild

def dump(root: Node) -> str:
    # Given in the prompt, not modifying this.
    #...
    #...

# ... [rest of the provided code]

# 1. Insert function:
def insert(root: Node, key: int) -> Node:
    if not root:
        return Node(key=key, keycount=1)
    if key < root.key:
        root.leftchild = insert(root.leftchild, key)
    elif key > root.key:
        root.rightchild = insert(root.rightchild, key)
    else:
        root.keycount += 1
    return root

# 2. Delete function:
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
            if not root.rightchild:
                return root.leftchild
            temp = _inorder_successor(root.rightchild)
            root.key = temp.key
            root.keycount = temp.keycount
            root.rightchild = delete(root.rightchild, temp.key)
    return root

def _inorder_successor(root: Node) -> Node:
    current = root
    while current.leftchild:
        current = current.leftchild
    return current

# 3. Search function:
def search(root: Node, search_key: int) -> str:
    path = []
    current = root
    while current:
        path.append(current.key)
        if current.key == search_key:
            break
        if search_key < current.key:
            current = current.leftchild
        else:
            current = current.rightchild
    return json.dumps(path, indent=2)

# 4. Preorder traversal:
def preorder(root: Node) -> str:
    result = []
    def _preorder(node):
        if node:
            result.append(node.key)
            _preorder(node.leftchild)
            _preorder(node.rightchild)
    _preorder(root)
    return json.dumps(result, indent=2)

# 5. Inorder traversal:
def inorder(root: Node) -> str:
    result = []
    def _inorder(node):
        if node:
            _inorder(node.leftchild)
            result.append(node.key)
            _inorder(node.rightchild)
    _inorder(root)
    return json.dumps(result, indent=2)

# 6. Postorder traversal:
def postorder(root: Node) -> str:
    result = []
    def _postorder(node):
        if node:
            _postorder(node.leftchild)
            _postorder(node.rightchild)
            result.append(node.key)
    _postorder(root)
    return json.dumps(result, indent=2)

# 7. Breadth-first traversal:
def bft(root: Node) -> str:
    if not root:
        return json.dumps([])
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
