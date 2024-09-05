class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def _binary_search_tree(self, arr):
        if len(arr) == 0:
            return None
        left = 0
        right = len(arr)
        mid = (left + right) // 2
        root = Node(arr[mid])
        root.left = self._binary_search_tree(arr[:mid])
        root.right = self._binary_search_tree(arr[mid + 1:])

        return root

    def find_node(self, node, p):
        if not node:
            return
        if node == p:
            return node
        if node.val > p.val:
            return self.find_node(node.left, p)
        return self.find_node(node.right, p)

    def recurse_from_root(self, node, p):
        if not node:
            return
        self.recurse_from_root(node.left, p)

        if self.previous == p and not self.answer:
            self.answer = node
            return

        if self.previous == p:
            self.previous = node
            return node

        self.previous = node

        self.recurse_from_root(node.right, p)

    def successor(self, root, p):
        node = self.find_node(root, p)
        self.answer = None
        if not node:
            return None
        if node.right:
            leftmost = node.right
            while leftmost.left:
                leftmost = leftmost.left
            self.answer = leftmost
        else:
            self.previous = None
            self.recurse_from_root(root, p)
        return self.answer


arr = [2, 1, 3]

solution = Solution()
head = solution._binary_search_tree(arr)
assert solution.successor(head, head) == head.right

arr = [5, 3, 6, 2, 4, 1]

head = solution._binary_search_tree(arr)

assert solution.successor(head, head.right.left) == head.right.right
