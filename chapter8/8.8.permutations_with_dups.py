class Solution:
    def __init__(self):
        self.answer = set()

    def permutations_with_dups(self, nums):
        def backtrack(permutation, indices):
            if len(permutation) == len(nums):
                self.answer.add(tuple(permutation[:]))
                return

            for i, num in enumerate(nums):
                if i not in indices:
                    permutation.append(num)
                    indices.add(i)
                    backtrack(permutation, indices)
                    permutation.pop()
                    indices.remove(i)

        backtrack([], set())
        return [list(i) for i in self.answer]


arr = [1, 1, 2]
solution = Solution()
answer = solution.permutations_with_dups(arr)
expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
assert sorted(answer) == sorted(expected)
arr = [1, 2, 3]
solution = Solution()
answer = solution.permutations_with_dups(arr)
expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
assert sorted(answer) == sorted(expected)
