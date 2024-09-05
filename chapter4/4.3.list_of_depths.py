class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class LinkedListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node


class Solution:

    def binary_search_tree(self, arr):
        if len(arr) == 0:
            return []
        left = 0
        right = len(arr)
        mid = (left + right) // 2
        root = Node(arr[mid])
        root.left = self.binary_search_tree(arr[:mid])
        root.right = self.binary_search_tree(arr[mid + 1:])

        return root

    def list_of_depths(self, tree):

        answer = []
        queue = [tree]
        while queue:
            head = LinkedListNode()
            dummy = head
            for _ in range(len(queue)):
                node = queue.pop(0)
                dummy.next_node = LinkedListNode(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                dummy = dummy.next_node
            answer.append(head.next_node)
        return answer


arr = [-10, -3, 0, 5, 9]

solution = Solution()
binary_tree = solution.binary_search_tree(arr)
answer = solution.list_of_depths(binary_tree)

assert answer[0].val == 0
assert answer[1].val == -3 and answer[1].next_node.val == 9
assert answer[2].val == -10 and answer[2].next_node.val == 5
