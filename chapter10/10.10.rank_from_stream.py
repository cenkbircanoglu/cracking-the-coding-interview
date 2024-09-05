class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.left_size = 0  # Tracks the number of nodes in the left subtree
        self.count = 1  # Tracks the number of times the value appears


class RankStream:
    def __init__(self):
        self.root = None

    def track(self, x):
        """Insert x into the stream."""
        if not self.root:
            self.root = TreeNode(x)
        else:
            self._insert(self.root, x)

    def _insert(self, node, x):
        if x == node.value:
            node.count += 1
        elif x < node.value:
            node.left_size += 1
            if node.left:
                self._insert(node.left, x)
            else:
                node.left = TreeNode(x)
        else:
            if node.right:
                self._insert(node.right, x)
            else:
                node.right = TreeNode(x)

    def get_rank_of_number(self, x):
        """Return the rank of x."""
        return self._get_rank(self.root, x)

    def _get_rank(self, node, x):
        if not node:
            return 0

        if x == node.value:
            return node.left_size + node.count
        elif x < node.value:
            return self._get_rank(node.left, x)
        else:
            return node.left_size + node.count + self._get_rank(node.right, x)


# Example usage:
stream = RankStream()
numbers = [5, 1, 4, 4, 5, 9, 7, 13, 3]

for number in numbers:
    stream.track(number)

print(stream.get_rank_of_number(4))  # Output: 4
print(stream.get_rank_of_number(13))  # Output: 9
print(stream.get_rank_of_number(5))  # Output: 6
