class Solution:
    def countBits(self, n: int) -> List[int]:
        b=[0]
        for i in range(1,n+1):
            c=bin(i)[2::].count('1')
            b.append(c)
        return b


            