class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return -1

        for i in range (len(haystack) + 1 - len(needle)):
            # for j in range (len(needle)):
            #     if haystack[i + j] != needle[j]:
            #         break
            #     if j == len(needle) - 1:
            #         return i

            if haystack[i: i + len(needle)] == needle:
                return i

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna