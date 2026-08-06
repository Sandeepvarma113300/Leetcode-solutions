class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            p = 1
            while temp != 0:
                digit = temp % 10
                p *= digit
                temp //= 10
            if p % t == 0:
                return n
            n += 1