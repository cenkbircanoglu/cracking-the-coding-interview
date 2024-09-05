class Solution:
    def english_int(self, num):
        if num == 0:
            return "Zero"

        # Define the word lists for numbers.
        below_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']

        def helper(n):
            if n == 0:
                return ''
            elif n < 20:
                return below_20[n] + ' '
            elif n < 100:
                return tens[n // 10] + ' ' + helper(n % 10)
            else:
                return below_20[n // 100] + ' Hundred ' + helper(n % 100)

        result = ''
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                result = helper(num % 1000) + unit + ' ' + result
            num //= 1000

        return result.strip()


solution = Solution()
assert solution.english_int(123) == "One Hundred Twenty Three"
assert solution.english_int(12345) == "Twelve Thousand Three Hundred Forty Five"
assert solution.english_int(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
