class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0
        def palindromeCheck(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            length = right - left - 1

            if length > max_len:
                max_len = length
                start = left + 1

        for i in range(len(s)):
            palindromeCheck(i, i)      # odd
            palindromeCheck(i, i + 1)  # even

        return s[start:start + max_len]