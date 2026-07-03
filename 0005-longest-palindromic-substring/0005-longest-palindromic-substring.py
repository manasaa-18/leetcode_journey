class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)      # odd-length palindrome
            len2 = self.expandAroundCenter(s, i, i + 1)  # even-length palindrome
            max_len = max(len1, len2)

            if max_len > end - start + 1:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna