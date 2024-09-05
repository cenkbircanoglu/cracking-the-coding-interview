class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def check_tree_equal(self, tree1, tree2):
        if tree1 is None or tree2 is None:
            return tree1 is None and tree2 is None
        return (
                (tree1.val == tree2.val)
                and self.check_tree_equal(tree1.left, tree2.left)
                and self.check_tree_equal(tree1.right, tree2.right)
        )

    def check_subtree(self, root, subRoot):
        queue = [root]

        while queue:
            new_queue = []
            for node in queue:
                if node:
                    if node.val == subRoot.val:
                        result = self.check_tree_equal(node, subRoot)
                        if result:
                            return True
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            queue = new_queue
        return False


head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.right.left = Node(4)
head.right.right = Node(6)

solution = Solution()
assert solution.check_subtree(head, head.right) == True
assert solution.check_subtree(head, head.right.left) == True
