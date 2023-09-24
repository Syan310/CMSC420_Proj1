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

def delete(root: Node, key: int) -> Node:
    if not root:
        return root
    if root.key == key:
        root.keycount -= 1
        if root.keycount == 0:
            if not root.leftchild:
                temp = root.rightchild
                root = None
                return temp
            elif not root.rightchild:
                temp = root.leftchild
                root = None
                return temp
            temp = find_min(root.rightchild)
            root.key = temp.key
            root.keycount = temp.keycount
            root.rightchild = delete(root.rightchild, temp.key)
    elif root.key > key:
        root.leftchild = delete(root.leftchild, key)
    else:
        root.rightchild = delete(root.rightchild, key)
    return root

def find_min(node):
    current = node
    while current.leftchild:
        current = current.leftchild
    return current

def search(root: Node, search_key: int) -> str:
    path = []
    current = root
    while current:
        path.append(current.key)
        if current.key == search_key:
            break
        elif current.key > search_key:
            current = current.leftchild
        else:
            current = current.rightchild
    return json.dumps(path, indent=2)

def preorder(root: Node) -> str:
    result = []
    if root:
        result.append(root.key)
        result.extend(json.loads(preorder(root.leftchild)))
        result.extend(json.loads(preorder(root.rightchild)))
    return json.dumps(result, indent=2)

def inorder(root: Node) -> str:
    result = []
    if root:
        result.extend(json.loads(inorder(root.leftchild)))
        result.append(root.key)
        result.extend(json.loads(inorder(root.rightchild)))
    return json.dumps(result, indent=2)

def postorder(root: Node) -> str:
    result = []
    if root:
        result.extend(json.loads(postorder(root.leftchild)))
        result.extend(json.loads(postorder(root.rightchild)))
        result.append(root.key)
    return json.dumps(result, indent=2)

def bft(root: Node) -> str:
    result = []
    if root:
        queue = [root]
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.leftchild:
                queue.append(current.leftchild)
            if current.rightchild:
                queue.append(current.rightchild)
    return json.dumps(result, indent=2)
