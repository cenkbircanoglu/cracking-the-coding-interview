from collections import Counter


class Solution:
    def pairs_with_sum(self, nums, target):
        cnt = Counter()
        ans = []
        for x in nums:
            y = target - x
            if cnt[y]:
                cnt[y] -= 1
                ans.append(sorted([x, y]))
            else:
                cnt[x] += 1

        return ans


solution = Solution()
expected = [[1, 7], [2, 6], [3, 5]]
answer = solution.pairs_with_sum([1, 2, 3, 4, 5, 6, 7], 8)
assert len(answer) == len(expected)
for pair in answer:
    assert pair in expected
