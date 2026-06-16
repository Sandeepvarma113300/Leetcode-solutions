class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        c=0
        window=s[:k]
        for i in window:
            if i in v:
                c=c+1
        max_count=c
        for i in range(k,len(s)):
            if s[i-k] in v:
                c=c-1
            if s[i] in v:
                c=c+1
            max_count=max(c,max_count)
        return max_count