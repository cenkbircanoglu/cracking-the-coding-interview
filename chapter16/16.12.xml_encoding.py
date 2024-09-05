class Solution:
    def xml_encoding(self, input_string):
        xml_chars = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&apos;'
        }

        # Build the encoded string by replacing special characters
        encoded_string = []
        for char in input_string:
            if char in xml_chars:
                encoded_string.append(xml_chars[char])
            else:
                encoded_string.append(char)

        # Join the list of characters back into a single string
        return ''.join(encoded_string)


input_str = 'Hello & welcome to <Coding> "Interview"'
solution = Solution()
assert solution.xml_encoding(input_str) == 'Hello &amp; welcome to &lt;Coding&gt; &quot;Interview&quot;'