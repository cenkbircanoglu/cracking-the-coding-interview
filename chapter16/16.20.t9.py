class Solution:
    def t9(self, digits, words):
        t9_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def is_valid_word(word):
            if len(word) != len(digits):
                return False
            for i, char in enumerate(word):
                if char not in t9_map[digits[i]]:
                    return False
            return True

        # Filter words in the dictionary that match the T9 digit sequence
        valid_words = [word for word in words if is_valid_word(word)]
        return valid_words


# Example usage
words = ["tree", "used", "hello", "meet", "go", "me", "good"]
digits = "8733"  # 'tree' or 'used'
solution = Solution()
assert solution.t9(digits, words) == ['tree', 'used']
