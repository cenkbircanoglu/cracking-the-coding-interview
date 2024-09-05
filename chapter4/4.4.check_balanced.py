class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def check_balanced(self, root):
        def calculate_depth(node, depth):
            if not node:
                return depth

            left_depth = calculate_depth(node.left, depth + 1)
            right_depth = calculate_depth(node.right, depth + 1)

            return max(left_depth, right_depth)

        if abs(calculate_depth(root.left, 0) - calculate_depth(root.right, 0)) <= 1:
            return True
        return False


head = Node(1)
head.left = Node(2)
head.left.left = Node(2)
head.left.left.left = Node(2)
head.right = Node(2)
head.right.left = Node(2)
head.right.right = Node(2)

solution = Solution()

assert solution.check_balanced(head) == True

head.left.left.left.left = Node(2)
head.left.left.left.left.left = Node(2)

assert solution.check_balanced(head) == False

head = Node(1)
head.left = Node(2)
head.left.left = Node(2)
head.left.left.left = Node(2)
head.right = Node(2)

assert solution.check_balanced(head) == False
