#Gonzales, Karla Grace P.

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


def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


def height(node):
    """Height in edges; empty tree -> -1, single node -> 0."""
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def iterative_size(root):
    if root is None:
        return 0
    count = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count


if __name__ == "__main__":
    root = build_tree()
    print(f"size = {size(root)}, height = {height(root)}")
    print(f"iterative_size = {iterative_size(root)}")
