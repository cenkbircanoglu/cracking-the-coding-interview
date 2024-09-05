class Solution:
    def one_away(self, str1, str2):
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        ind1, ind2 = 0, 0
        found_difference = False

        while ind2 < len(str2) and ind1 < len(str1):
            if str1[ind1] != str2[ind2]:
                if found_difference:
                    return False
                found_difference = True
                if len(str1) == len(str2):
                    ind1 += 1
            else:
                ind1 += 1
            ind2 += 1

        return True


solution = Solution()

assert solution.one_away("pale", "ple") == True
assert solution.one_away("pales", "pale") == True
assert solution.one_away("pale", "bale") == True
assert solution.one_away("pale", "bake") == False
