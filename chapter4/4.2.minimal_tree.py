class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def binary_search_tree(self, arr):
        if len(arr) == 0:
            return None
        left = 0
        right = len(arr)
        mid = (left + right) // 2
        root = Node(arr[mid])
        root.left = self.binary_search_tree(arr[:mid])
        root.right = self.binary_search_tree(arr[mid + 1:])

        return root


arr = [1, 2, 3, 4, 5]

solution = Solution()
root = solution.binary_search_tree(arr)
assert root.left.left.val == 1
assert root.left.val == 2
assert root.val == 3
assert root.right.left.val == 4
assert root.right.val == 5

arr = [1, 2, 3, 4, 5, 6]

solution = Solution()
root = solution.binary_search_tree(arr)
assert root.left.left.val == 1
assert root.left.val == 2
assert root.left.right.val == 3
assert root.val == 4
assert root.right.left.val == 5
assert root.right.val == 6

arr = [-10, -3, 0, 5, 9]

solution = Solution()
root = solution.binary_search_tree(arr)
assert root.left.left.val == -10
assert root.left.val == -3
assert root.val == 0
assert root.right.left.val == 5
assert root.right.val == 9
