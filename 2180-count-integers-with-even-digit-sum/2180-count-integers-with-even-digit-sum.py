class Solution:
    def countEven(self, num: int) -> int:
        c = 0
        for i in range(1, num + 1):
            s = 0
            temp = i   
            while temp != 0:
                r = temp % 10
                s += r
                temp //= 10
            if s % 2 == 0:
                c += 1
        return c



