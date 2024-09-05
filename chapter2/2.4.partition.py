class LinkedListNode:

    def __init__(self, val = None):
        self.val = val
        self.next = None

class Solution:

    def partition(self, node, k):
        left_head = LinkedListNode()
        mid_head = LinkedListNode()
        right_head = LinkedListNode()

        left = left_head
        mid = mid_head
        right = right_head

        curr = head

        while curr:
            if curr.val < k:
                left.next = curr
                left = left.next
            elif curr.val == k:
                mid.next = curr
                mid = mid.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next

        # Connect the partitions together
        right.next = None

        # Connect mid to right
        mid.next = right_head.next

        # Connect less to mid
        left.next = mid_head.next

        # New head of the rearranged list
        new_head = left_head.next

        return new_head




solution = Solution()

head = LinkedListNode(3)
head.next = LinkedListNode(5)
head.next.next = LinkedListNode(8)
head.next.next.next = LinkedListNode(5)
head.next.next.next.next = LinkedListNode(10)
head.next.next.next.next.next = LinkedListNode(2)
head.next.next.next.next.next.next = LinkedListNode(1)

answer = solution.partition(head, 5)
expected = [3, 2, 1, 5, 5, 8, 10]
i = 0
while answer:
    assert answer.val == expected[i]
    i += 1
    answer = answer.next

