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
        return root
    
    # Recursive cases
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
            temp = get_min(root.rightchild)
            root.key, root.keycount = temp.key, temp.keycount
            root.rightchild = delete(root.rightchild, temp.key)
    return root

def get_min(node):
    current = node
    while current.leftchild:
        current = current.leftchild
    return current

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

def preorder(root: Node) -> str:
    def traverse(node):
        if not node:
            return []
        return [node.key] + traverse(node.leftchild) + traverse(node.rightchild)

    return json.dumps(traverse(root), indent=2)

def inorder(root: Node) -> str:
    def traverse(node):
        if not node:
            return []
        return traverse(node.leftchild) + [node.key] + traverse(node.rightchild)

    return json.dumps(traverse(root), indent=2)

def postorder(root: Node) -> str:
    def traverse(node):
        if not node:
            return []
        return traverse(node.leftchild) + traverse(node.rightchild) + [node.key]

    return json.dumps(traverse(root), indent=2)

def bft(root: Node) -> str:
    if not root:
        return json.dumps([], indent=2)
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current.key)
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)
    return json.dumps(result, indent=2)
