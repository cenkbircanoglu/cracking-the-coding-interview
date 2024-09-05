class LinkedListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:

    def reverse(self, head):
        current = head
        previous = None
        while current:
            current.next, current, previous = previous, current.next, current
        return previous

    def find_mid(self, head):
        fast, slow = head, head
        previous = None
        while fast and fast.next:
            fast = fast.next.next
            previous = slow
            slow = slow.next
        previous.next = None
        return slow

    def is_palindrome(self, head):
        mid = self.find_mid(head)
        reverse = self.reverse(mid)

        while head and reverse:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next

        return True


solution = Solution()

head = LinkedListNode(7)
head.next = LinkedListNode(1)
head.next.next = LinkedListNode(7)

assert solution.is_palindrome(head) == True

head = LinkedListNode(7)
head.next = LinkedListNode(1)
head.next.next = LinkedListNode(1)
head.next.next.next = LinkedListNode(7)

assert solution.is_palindrome(head) == True

head = LinkedListNode(7)
head.next = LinkedListNode(1)
head.next.next = LinkedListNode(6)

assert solution.is_palindrome(head) == False

head = LinkedListNode(7)
head.next = LinkedListNode(1)
head.next.next = LinkedListNode(1)
head.next.next.next = LinkedListNode(1)

assert solution.is_palindrome(head) == False
