class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = s.lower()

        t = ""
        for i in c:
            if i.isalnum():
                t += i

        p = 0
        q = len(t) - 1

        while p < q:
            if t[p] != t[q]:
                return False
            p += 1
            q -= 1

        return True