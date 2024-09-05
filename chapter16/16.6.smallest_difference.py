import math


class Solution:
    def smallest_difference(self, nums1, nums2):
        if len(nums2) > len(nums1):
            return self.smallest_difference(nums2, nums1)
        nums1.sort()
        nums2.sort()
        answer = math.inf
        for num2 in nums2:
            left = 0
            right = len(nums1) - 1
            while left < right:
                mid = (left + right) // 2
                if nums1[mid] < num2:
                    left = mid + 1
                else:
                    right = mid
            answer = min(answer, abs(num2 - nums1[left]), abs(num2 - nums1[right]))
        return answer


nums1 = [1, 3, 15, 11, 2]
nums2 = [23, 127, 235, 19, 8]
expected = 3
solution = Solution()
assert solution.smallest_difference(nums1, nums2) == expected

nums1 = [1, 3, 15, 11, 2]
nums2 = [23, 127, 235, 19]
expected = 4
solution = Solution()

assert solution.smallest_difference(nums1, nums2) == expected
