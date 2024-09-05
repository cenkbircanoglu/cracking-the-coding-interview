from collections import defaultdict


from collections import defaultdict
from re import I, S
class Solution:

    def palindrome_permutation(self, string):
        counter = {}

        for c in string:
            if c == " ":
                continue
            if c.isalpha():
                c = c.lower()
            if c in counter:
                del counter[c]
            else:
                counter[c] = 1

        return len(counter) <= 1

string = "Taco cat"
solution = Solution()
assert solution.palindrome_permutation(string) == True

string = "TacecAt"
assert solution.palindrome_permutation(string) == True

string = "Taeecet"
assert solution.palindrome_permutation(string) == False

string = ""
assert solution.palindrome_permutation(string) == True

string = "a"
assert solution.palindrome_permutation(string) == True


