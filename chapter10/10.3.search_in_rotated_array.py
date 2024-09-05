class Solution:
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def find_min_value_index(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[len(nums) - 1]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def search_in_rotated_array(self, nums, target):
        min_index = self.find_min_value_index(nums)
        if target > nums[-1]:
            return self.binary_search(nums[:min_index], target)
        else:
            return self.binary_search(nums[min_index:], target) + min_index

solution = Solution()
nums = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
target = 5
assert solution.search_in_rotated_array(nums, target) == 8

target = 16
assert solution.search_in_rotated_array(nums, target) == 1

target = 19
assert solution.search_in_rotated_array(nums, target) == 2

target = 1
assert solution.search_in_rotated_array(nums, target) == 5
