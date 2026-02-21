class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        c = 0
        
        for i in range(left, right + 1):
            setbits = bin(i).count('1')
            if isPrime(setbits):
                c += 1
        return c