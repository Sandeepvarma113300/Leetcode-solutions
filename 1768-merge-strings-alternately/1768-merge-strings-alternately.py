class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        r=0
        b=[]
        while l<len(word1) and r<len(word2):
            b.append(word1[l])
            b.append(word2[r])
            l=l+1
            r=r+1
        while l<len(word1):
            b.append(word1[l])
            l=l+1
        while r<len(word2):
            b.append(word2[r])
            r=r+1
        return "".join(b)


