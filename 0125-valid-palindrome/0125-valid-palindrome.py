class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        def fun(i, j):
            if i >= j:              
                return True
            if s[i] != s[j]:
                return False
            return fun(i + 1, j - 1) 
        
        return fun(0, len(s) - 1)
