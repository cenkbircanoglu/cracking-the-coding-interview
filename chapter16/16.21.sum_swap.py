class Solution:
    def sum_swap(self, nums1, nums2):
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        diff = sum1 - sum2
        if diff % 2 != 0:
            return None
        target_diff = diff // 2
        nums2_set = set(nums2)

        for num1 in nums1:
            b = num1 - target_diff
            if b in nums2_set:
                return [num1, b]

        return None


solution = Solution()
assert solution.sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]) in [[1, 3], [2, 4], [4, 6]]
