class Solution:

    def string_compression(self, string):
        if not string:
            return ""
        last_char = string[0]
        count = 1
        answer = []
        for i in range(1, len(string)):
            if string[i] == last_char:
                count += 1
            else:
                answer.append(last_char)
                answer.append(str(count))
                count = 1
                last_char = string[i]
        answer.append(last_char)
        answer.append(str(count))

        return "".join(answer)


string = "aabcccccaaa"
solution = Solution()

assert solution.string_compression(string) == "a2b1c5a3"
