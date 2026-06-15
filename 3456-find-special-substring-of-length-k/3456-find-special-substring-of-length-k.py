class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        c=1
        for i in  range(1,len(s)):
            if s[i]==s[i-1]:
                c=c+1
            else:
                if c==k:
                    return True
                c=1
        if c==k:
            return True
        return False