class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        b=['']*len(s)
        for i in range(len(indices)):
            b[indices[i]]=s[i]
        return "".join(b)