#Gonzales, Karla Grace P.
#BSIT

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    root = Node(15)
    root.left, root.right = Node(10), Node(25)
    root.left.left, root.left.right = Node(4), Node(12)
    root.right.left, root.right.right = Node(20), Node(30)
    root.left.left.left, root.left.left.right = Node(2), Node(6)
    return root


def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.data)
    inorder(node.right, out)


def preorder(node, out):
    if node is None:
        return
    out.append(node.data)
    preorder(node.left, out)
    preorder(node.right, out)


def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.data)


def level_order(root):
    out = []
    if root is None:
        return out
    queue = deque([root])
    while queue:
        node = queue.popleft()
        out.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return out


def show(label, values):
    print(f"{label}: " + " ".join(map(str, values)))


if __name__ == "__main__":
    root = build_tree()
    res = []; inorder(root, res); show("Inorder", res)
    res = []; preorder(root, res); show("Preorder", res)
    res = []; postorder(root, res); show("Postorder", res)
    show("Level-order", level_order(root))
