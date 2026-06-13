class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        p = 0
        q = len(s) - 1
        while p < q:
            if s[p] != s[q]:
                return isPalindrome(p + 1, q) or isPalindrome(p, q - 1)
            p += 1
            q -= 1
        return True