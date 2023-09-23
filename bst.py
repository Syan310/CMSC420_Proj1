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
    if root is None:
        return Node(key=key, keycount=1)
    if key < root.key:
        root.leftchild = insert(root.leftchild, key)
    elif key > root.key:
        root.rightchild = insert(root.rightchild, key)
    else:  # key is already in the tree.
        root.keycount += 1
    return root

def find_min_node(node: Node) -> Node:
    current = node
    while current.leftchild is not None:
        current = current.leftchild
    return current

def delete(root: Node, key: int) -> Node:
    if root is None:
        return root
    if key < root.key:
        root.leftchild = delete(root.leftchild, key)
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    else:
        if root.keycount > 1:
            root.keycount -= 1
        else:
            if root.leftchild is None:
                return root.rightchild
            elif root.rightchild is None:
                return root.leftchild
            temp = find_min_node(root.rightchild)
            root.key = temp.key
            root.keycount = temp.keycount
            root.rightchild = delete(root.rightchild, temp.key)
    return root

def search(root: Node, search_key: int) -> str:
    path = []
    current = root
    while current is not None:
        path.append(current.key)
        if search_key < current.key:
            current = current.leftchild
        elif search_key > current.key:
            current = current.rightchild
        else:
            break  # key is found.
    return json.dumps(path, indent=2)

def preorder(root: Node) -> str:
    result = []
    if root:
        result.append(root.key)
        result.extend(json.loads(preorder(root.leftchild)))
        result.extend(json.loads(preorder(root.rightchild)))
    return json.dumps(result)

def inorder(root: Node) -> str:
    result = []
    if root:
        result.extend(json.loads(inorder(root.leftchild)))
        result.append(root.key)
        result.extend(json.loads(inorder(root.rightchild)))
    return json.dumps(result)

def postorder(root: Node) -> str:
    result = []
    if root:
        result.extend(json.loads(postorder(root.leftchild)))
        result.extend(json.loads(postorder(root.rightchild)))
        result.append(root.key)
    return json.dumps(result)

def bft(root: Node) -> str:
    result = []
    if root is None:
        return json.dumps(result)
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        result.append(node.key)
        if node.leftchild is not None:
            queue.put(node.leftchild)
        if node.rightchild is not None:
            queue.put(node.rightchild)
    return json.dumps(result)
