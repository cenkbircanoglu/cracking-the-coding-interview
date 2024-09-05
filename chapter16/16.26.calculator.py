class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        x = 0
        sign = "+"
        stack = []
        for i, c in enumerate(s):
            if c.isdigit():
                x = x * 10 + ord(c) - ord("0")
            if i == n - 1 or c in "+-*/":
                match sign:
                    case "+":
                        stack.append(x)
                    case "-":
                        stack.append(-x)
                    case "*":
                        stack.append(stack.pop() * x)
                    case "/":
                        stack.append(int(stack.pop() / x))
                x = 0
                sign = c
        return sum(stack)


solution = Solution()

assert solution.calculate("3+2*2") == 7
assert solution.calculate("3/2") == 1
