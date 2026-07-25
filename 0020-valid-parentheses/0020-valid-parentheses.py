class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return not stack #checks if stack is empty

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna