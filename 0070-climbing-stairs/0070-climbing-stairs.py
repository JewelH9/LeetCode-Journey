class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range (n-1):
            temp = one
            one = one + two
            two = temp

        return one

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna