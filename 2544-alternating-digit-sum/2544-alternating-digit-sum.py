class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        t=0
        for i in range(len(s)):
            d=int(s[i])
            if i%2==0:
                t=t+d
            else:
                t=t-d
        return t