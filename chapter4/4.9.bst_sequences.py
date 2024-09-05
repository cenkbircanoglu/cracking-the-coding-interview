class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def weave_lists(self, first, second, results, prefix):
        if len(first) == 0 or len(second) == 0:
            result = prefix[:]
            result.extend(first)
            result.extend(second)
            results.append(result)
            return

        head_first = first.pop(0)
        prefix.append(head_first)
        self.weave_lists(first, second, results, prefix)
        prefix.pop()
        first.insert(0, head_first)

        # Do the same thing with second, damaging and then restoring the list
        head_second = second.pop(0)
        prefix.append(head_second)
        self.weave_lists(first, second, results, prefix)
        prefix.pop()
        second.insert(0, head_second)

    def bst_sequences(self, node):
        result = []

        if node is None:
            return [[]]

        prefix = [node.value]

        left_seq = self.bst_sequences(node.left)
        right_seq = self.bst_sequences(node.right)

        for left in left_seq:
            for right in right_seq:
                weaved = []
                self.weave_lists(left, right, weaved, prefix)
                result.extend(weaved)

        return result


# Example usage
head = Node(2)
head.left = Node(1)
head.right = Node(3)

solution = Solution()

result = solution.bst_sequences(head)
for seq in result:
    print(seq)
