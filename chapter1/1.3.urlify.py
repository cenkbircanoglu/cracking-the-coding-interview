class Solution:
    def urlify(self, string, true_length):
        num_spaces = string.count(" ")
        new_index = true_length - 1 + num_spaces * 2
        string = list(string)
        answer = [''] * (new_index + 1)
        for i in range(true_length - 1, -1, -1):
            if string[i] == " ":
                answer[new_index] = "0"
                answer[new_index - 1] = "2"
                answer[new_index - 2] = "%"
                new_index -= 3
            else:
                answer[new_index] = string[i]
                new_index -= 1
        return "".join(answer)


string = "Mr John Smith"
len_string = 13

solution = Solution()
assert solution.urlify(string, len_string) == "Mr%20John%20Smith"

string = "ME Jo Smith"
len_string = 11

solution = Solution()
assert solution.urlify(string, len_string) == "ME%20Jo%20Smith"
