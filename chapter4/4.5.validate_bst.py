import math


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def validate_bst(self, root):
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val > high or node.val < low:
                return False
            return validate(node.left, high=node.val, low=low) and validate(node.right, low=node.val, high=high)

        return validate(root)


head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.right.left = Node(4)
head.right.right = Node(6)

solution = Solution()

assert solution.validate_bst(head) == True

head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.right.left = Node(4)
head.right.right = Node(6)
head.right.right.right = Node(6)
head.right.right.right.right = Node(6)
head.right.right.right.right.right = Node(6)
head.right.right.right.right.right.right = Node(6)

assert solution.validate_bst(head) == True

head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.right.left = Node(2)
head.right.right = Node(6)
head.right.right.right = Node(6)
head.right.right.right.right = Node(6)
head.right.right.right.right.right = Node(6)
head.right.right.right.right.right.right = Node(6)

assert solution.validate_bst(head) == False

head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.left.left = Node(3)
head.right.right = Node(6)
head.right.right.right = Node(6)
head.right.right.right.right = Node(6)
head.right.right.right.right.right = Node(6)
head.right.right.right.right.right.right = Node(6)

assert solution.validate_bst(head) == False
