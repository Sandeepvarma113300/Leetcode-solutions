class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        p="aeiou"
        c=0
        for i in range(k):
            if s[i] in p:
                c=c+1
        max_count=c
        for i in range(k,len(s)):
            if s[i-k] in p:
                c=c-1
            if s[i] in p:
                c=c+1
            max_count=max(max_count,c)
        return max_count
