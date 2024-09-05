class Helper:
    def __init__(self, arr):
        self.arr = arr

    def element_at(self, i):
        if i < len(self.arr):
            return self.arr[i]
        return -1


class Solution:
    def sorted_search_no_size(self, helper, target):
        left = 0
        right = 2
        while left <= right:
            mid = (left + right) // 2
            answer = helper.element_at(mid)
            if answer == target:
                return mid
            elif answer > target or answer == -1:
                right = mid - 1
            else:
                left = mid + 1
                right *= 2
        return -1


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
helper = Helper(arr)
solution = Solution()
assert solution.sorted_search_no_size(helper, 6) == 6

arr = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
helper = Helper(arr)
solution = Solution()
assert solution.sorted_search_no_size(helper, 60) == 6
assert solution.sorted_search_no_size(helper, 6) == -1
