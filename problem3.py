#Gonzales, Karla

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:      
                return node.right
            if node.right is None:    
                return node.left
            successor = node.right  
            while successor.left:
                successor = successor.left
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node

    def inorder(self):
        result = []

        def walk(node):
            if node is None:
                return
            walk(node.left)
            result.append(node.key)
            walk(node.right)

        walk(self.root)
        return result


if __name__ == "__main__":
    bst = BST()
    for key in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        bst.insert(key)
    print(bst.inorder())   
    print(bst.search(35))  
    print(bst.search(99))  
    bst.delete(20)         
    bst.delete(40)         
    print(bst.inorder())
