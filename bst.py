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
        return None
    if key == root.key:
        root.keycount -= 1
        if root.keycount == 0:
            # Node with only one child or no child
            if not root.leftchild:
                return root.rightchild
            elif not root.rightchild:
                return root.leftchild
            # Node with two children
            root.key = minValue(root.rightchild)
            root.rightchild = delete(root.rightchild, root.key)
    elif key < root.key:
        root.leftchild = delete(root.leftchild, key)
    else:
        root.rightchild = delete(root.rightchild, key)
    return root

def minValue(node):
    current = node
    while current.leftchild is not None:
        current = current.leftchild
    return current.key

def search(root: Node, search_key: int) -> str:
    path = []
    while root:
        path.append(root.key)
        if search_key == root.key:
            break
        elif search_key < root.key:
            root = root.leftchild
        else:
            root = root.rightchild
    return json.dumps(path, indent=2)

def preorder(root: Node) -> str:
    def traverse(node):
        if node:
            keys.append(node.key)
            traverse(node.leftchild)
            traverse(node.rightchild)
    keys = []
    traverse(root)
    return json.dumps(keys, indent=2)

def inorder(root: Node) -> str:
    def traverse(node):
        if node:
            traverse(node.leftchild)
            keys.append(node.key)
            traverse(node.rightchild)
    keys = []
    traverse(root)
    return json.dumps(keys, indent=2)

def postorder(root: Node) -> str:
    def traverse(node):
        if node:
            traverse(node.leftchild)
            traverse(node.rightchild)
            keys.append(node.key)
    keys = []
    traverse(root)
    return json.dumps(keys, indent=2)

def bft(root: Node) -> str:
    if not root:
        return json.dumps([], indent=2)
    keys, queue = [], [root]
    while queue:
        current = queue.pop(0)
        keys.append(current.key)
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)
    return json.dumps(keys, indent=2)
