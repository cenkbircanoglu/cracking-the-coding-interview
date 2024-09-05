class Solution:

    def find_magic_index(self, arr, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        # Check if mid is a magic index
        if arr[mid] == mid:
            return mid

        # Search left
        left_index = min(mid - 1, arr[mid])
        left_result = self.find_magic_index(arr, start, left_index)
        if left_result != -1:
            return left_result

        # Search right
        right_index = max(mid + 1, arr[mid])
        return self.find_magic_index(arr, right_index, end)

    def magic_index(self, arr):
        return self.find_magic_index(arr, 0, len(arr) - 1)


arr = [-10, 1, 3, 2, 6, 4, 5]
solution = Solution()
assert solution.magic_index(arr) == 1
arr = [-10, 1, 1, 1, 6, 4, 5]
solution = Solution()
assert solution.magic_index(arr) == 1