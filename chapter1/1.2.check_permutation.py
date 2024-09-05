from collections import defaultdict

class Solution:
    def check_permutation(self, str1, str2):
        if not str1 or not str2:
            return False
        counter = defaultdict(int)
        for c in str1:
            counter[c] += 1
        for c in str2:
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
        return len(counter) == 0


str1 = "abcde"
str2 = "edcab"
solution = Solution()
assert solution.check_permutation(str1, str2) == True
str2 = ""
assert solution.check_permutation(str1, str2) == False

str1 = "a" * 10
str2 = "a" * 9
assert solution.check_permutation(str1, str2) == False

str1 = "a  " * 10
str2 = "a" * 10
assert solution.check_permutation(str1, str2) == False
