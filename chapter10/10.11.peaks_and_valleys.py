# TODO
class Solution:

    def peaks_and_valleys(self, nums):
        # Sort the nums
        nums.sort()

        # Swap elements to create peaks and valleys
        for i in range(1, len(nums), 2):
            if i + 1 < len(nums):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums


nums = [5, 3, 1, 2, 3]
solution = Solution()
assert solution.peaks_and_valleys(nums) == [1, 3, 2, 5, 3]
