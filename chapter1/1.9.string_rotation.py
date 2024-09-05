class Solution:

    def string_rotation(self, str1, str2):

        if len(str1) != len(str2):
            return False
        first = 0
        second = 0
        possible_starts = []
        while second < len(str2):
            if str1[first] == str2[second]:
                possible_starts.append(second)
            second += 1
        str2 += str2

        for i in possible_starts:
            j = i
            rotated = True
            for c in str1:
                if c != str2[j]:
                    rotated = False
                    break
                j += 1
            if rotated:
                return True
        return False


string1 = "waterbottle"
string2 = "erbottlewat"

solution = Solution()
assert solution.string_rotation(string1, string2) == True
string2 = "rebottlewat"
assert solution.string_rotation(string1, string2) == False
