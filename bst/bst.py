class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return ' ' + str(self.data) + ' '


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        new_node = BSTNode(data)

        if root is None:
            root = new_node
            return root

        elif data < root.data:
            root.left = self.insert(root.left, data)

        else:
            root.right = self.insert(root.right, data)
        return root


    def in_order_walk(self, root):
        result = ''
        if root is not None:
            result += str(root.data)
            result +=  ' ' + self.in_order_walk(root.left)

            result += ' ' + self.in_order_walk(root.right)
        return result

    def __str__(self):
        return self.in_order_walk(self.root)

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.root = tree.insert(tree.root, 10)

    tree.insert(tree.root, 20)


    tree.insert(tree.root, 15)

    print(tree)
