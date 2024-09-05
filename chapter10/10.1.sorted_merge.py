class Solution:
    def sorted_merge(self, A, B):
        pointerA, pointerb = len(A) - 1, len(B) - 1
        while pointerA >= 0 and A[pointerA] is None:
            pointerA -= 1
        if pointerA < 0:
            A[:] = B
            return

        i = len(A) - 1
        while pointerb >= 0:
            if A[pointerA] and A[pointerA] > B[pointerb]:
                A[i] = A[pointerA]
                pointerA -= 1
            else:
                A[i] = B[pointerb]
                pointerb -= 1
            i -= 1


A = [1, 3, 5, 7, None, None, None, None]
B = [2, 4, 6, 8]
solution = Solution()
solution.sorted_merge(A, B)
expected = [1, 2, 3, 4, 5, 6, 7, 8]
assert A == expected

A = [1, 3, 5, 7, None, None, None, None]
B = [1, 3, 5, 7]
solution = Solution()
solution.sorted_merge(A, B)
expected = [1, 1, 3, 3, 5, 5, 7, 7]
assert A == expected

A = [None, None, None, None]
B = [1, 3, 5, 7]
solution = Solution()
solution.sorted_merge(A, B)
expected = [1, 3, 5, 7]
assert A == expected

A = [1, 3, 5, 7]
B = []
solution = Solution()
solution.sorted_merge(A, B)
expected = [1, 3, 5, 7]
assert A == expected
