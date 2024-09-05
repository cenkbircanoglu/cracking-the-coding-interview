class Solution:
    def __init__(self):
        self.answer = []

    def power_set(self, nums):
        def backtrack(start, path):

            self.answer.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

        return self.answer

arr = [1, 2]
solution = Solution()
answer = solution.power_set(arr)
expected = [[], [1], [2], [1, 2]]
assert sorted(answer) == sorted(expected)

arr = [1, 2, 3]
solution = Solution()
answer = solution.power_set(arr)
expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
assert sorted(answer) == sorted(expected)

arr = [1, 2, 3, 4]
solution = Solution()
answer = solution.power_set(arr)
expected = [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3],
             [1, 2, 4], [1, 3, 4],  [2, 3, 4], [1, 2, 3, 4]]
assert sorted(answer) == sorted(expected)
