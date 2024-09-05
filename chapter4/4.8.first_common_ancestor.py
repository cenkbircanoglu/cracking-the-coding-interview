class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def check_contains(self, node, target):
        if not node:
            return False
        if node == target:
            return True
        return self.check_contains(node.left, target) or self.check_contains(node.right, target)

    def first_common_ancestor(self, root, p, q):
        def FCA(node, p, q):
            if not node or node == p or node == q:
                return node
            left = FCA(node.left, p, q)
            right = FCA(node.right, p, q)
            if left and right:
                return node
            if left:
                return left
            return right

        answer = FCA(root, p, q)
        if answer == p:
            if self.check_contains(answer, q):
                return p
            return None
        elif answer == q:
            if self.check_contains(answer, p):
                return q
            return None
        return answer


head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.right.left = Node(4)
head.right.right = Node(6)

solution = Solution()
result = solution.first_common_ancestor(head, head.right.left, head.right.right)
assert result == head.right


result = solution.first_common_ancestor(head,head.right.left , head.right)
assert result == head.right

result = solution.first_common_ancestor(head,head.left , head.right.right)
assert result == head