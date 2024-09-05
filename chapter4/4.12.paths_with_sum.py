class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:

    def paths_with_sum(self, root, target):
        def preorder(node, curr_sum) -> None:
            if not node:
                return

            curr_sum += node.val
            if curr_sum == target:
                self.counts += 1
            self.counts += h[curr_sum - target]
            h[curr_sum] += 1
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            h[curr_sum] -= 1

        self.counts = 0
        h = defaultdict(int)
        preorder(root, 0)
        return self.counts


head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.right.left = Node(4)
head.right.right = Node(6)

solution = Solution()
assert solution.paths_with_sum(head, 5) == 2
assert solution.paths_with_sum(head, 6) == 1
assert solution.paths_with_sum(head, 4) == 1
