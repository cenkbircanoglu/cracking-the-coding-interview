class Solution:
    def __init__(self):
        self.answer = set()

    def permutations_without_dups(self, nums):
        n_unique = len(set(nums))

        def backtrack(permutation):
            if len(permutation) == n_unique:
                self.answer.add(tuple(permutation))
                return

            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    backtrack(permutation)
                    permutation.pop()

        backtrack([])
        return [list(i) for i in self.answer]


arr = [1, 1, 2]
solution = Solution()
answer = solution.permutations_without_dups(arr)
expected = [[1, 2], [2, 1]]
assert sorted(answer) == sorted(expected)

arr = [1, 2, 3]
solution = Solution()
answer = solution.permutations_without_dups(arr)
expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
assert sorted(answer) == sorted(expected)
