import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        s1=0
        s2=0
        r=(n+n)
        for i in range(r+1):
            if i%2==0:
                s1=s1+i
            else:
                s2=s2+i
        return math.gcd(s1,s2)
           