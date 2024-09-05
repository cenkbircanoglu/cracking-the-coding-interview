from collections import defaultdict


class Solution:

    def group_anagrams(self, strs):
        answer = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            answer[tuple(count)].append(s)

        return list(answer.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
solution = Solution()
answer = solution.group_anagrams(strs)
assert sorted(answer) == sorted(expected)
