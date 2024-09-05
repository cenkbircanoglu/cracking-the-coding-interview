class Solution:

    def is_unique(self, string):
        tmp = ord(string[0])
        for i in range(1, len(string)):
            tmp = tmp ^ ord(string[i])
            if tmp == 0:
                return False
        return True

solution = Solution()
assert solution.is_unique("abcde") == True
assert solution.is_unique("aabcde") == False
assert solution.is_unique("Aa") == True
assert solution.is_unique("abcde") == True
