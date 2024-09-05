class Solution:
    def contiguous_sequence(self, nums):
        max_sum = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum


solution = Solution()
assert solution.contiguous_sequence([2, -8, 3, -2, 4, -10]) == 5
