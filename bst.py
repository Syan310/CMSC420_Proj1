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
    if root.key == key:
        root.keycount += 1
    elif root.key > key:
        root.leftchild = insert(root.leftchild, key)
    else:
        root.rightchild = insert(root.rightchild, key)
    return root

def find_min(node: Node) -> Node:
    current = node
    while current.leftchild:
        current = current.leftchild
    return current

def delete(root: Node, key: int) -> Node:
    if not root:
        return root
    
    # Key is smaller, go left
    if key < root.key:
        root.leftchild = delete(root.leftchild, key)
    
    # Key is larger, go right
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    
    # Node with the key found
    else:
        if root.keycount > 1:
            root.keycount -= 1
            return root
        else:
            # Node with one child or no child
            if not root.leftchild:
                return root.rightchild
            if not root.rightchild:
                return root.leftchild
            
            # Node with two children, get the inorder successor (smallest in the right subtree)
            temp = find_min(root.rightchild)
            root.key = temp.key
            if temp.keycount > 1:
                temp.keycount -= 1
            else:
                root.rightchild = delete(root.rightchild, temp.key)
    
    return root



def search(root: Node, search_key: int) -> str:
    result = []
    current = root
    while current is not None:
        result.append(current.key)
        if search_key < current.key:
            current = current.leftchild
        elif search_key > current.key:
            current = current.rightchild
        else:
            break  # search_key found
    return json.dumps(result, indent=2)


def preorder(root: Node) -> str:
    result = []
    def _preorder_traversal(node):
        if node is not None:
            result.append(node.key)
            _preorder_traversal(node.leftchild)
            _preorder_traversal(node.rightchild)
    _preorder_traversal(root)
    return json.dumps(result, indent=2)


def inorder(root: Node) -> str:
    result = []
    def _inorder_traversal(node):
        if node is not None:
            _inorder_traversal(node.leftchild)
            result.append(node.key)
            _inorder_traversal(node.rightchild)
    _inorder_traversal(root)
    return json.dumps(result, indent=2)

def postorder(root: Node) -> str:
    result = []
    def _postorder_traversal(node):
        if node is not None:
            _postorder_traversal(node.leftchild)
            _postorder_traversal(node.rightchild)
            result.append(node.key)
    _postorder_traversal(root)
    return json.dumps(result, indent=2)

def bft(root: Node) -> str:
    if not root:
        return json.dumps([], indent=2)

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)  # dequeuing (removing from the front)
        result.append(node.key)
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)

    return json.dumps(result, indent=2)

