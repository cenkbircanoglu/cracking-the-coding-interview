import math


class Solution:
    def sub_sort(self, array):
        n = len(array)
        mi, mx = math.inf, -math.inf
        left = right = -1
        for i, x in enumerate(array):
            if x < mx:
                right = i
            else:
                mx = x
        for i in range(n - 1, -1, -1):
            if array[i] > mi:
                left = i
            else:
                mi = array[i]
        return [left, right]


solution = Solution()

assert solution.sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]) == [3, 9]
