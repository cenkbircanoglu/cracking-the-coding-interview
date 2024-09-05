from random import randint


class Node:

    def __init__(self, data):
        self.data = data
        self.children = 0
        self.left = None
        self.right = None


class Solution:
    def get_elements(self, root):
        if root == None:
            return 0

        return (self.get_elements(root.left) +
                self.get_elements(root.right) + 1)

    def count_children(self, root):
        if root == None:
            return

        root.children = self.get_elements(root) - 1
        self.count_children(root.left)
        self.count_children(root.right)

    def children(self, root):
        if root == None:
            return 0
        return root.children + 1

    def random_node_util(self, root, count):
        if root == None:
            return 0

        if count == self.children(root.left):
            return root.data

        if count < self.children(root.left):
            return self.random_node_util(root.left, count)

        return self.random_node_util(root.right,
                                     count - self.children(root.left) - 1)

    def random_node(self, root):
        count = randint(0, root.children)
        return self.random_node_util(root, count)


# Driver Code
head = Node(1)
head.left = Node(2)
head.right = Node(3)
head.left.right = Node(4)
head.left.right = Node(5)
head.right.left = Node(6)
head.right.right = Node(7)
solution = Solution()
solution.count_children(head)

res = solution.random_node(head)

assert res in [1, 2, 3, 4, 5, 6, 7]
