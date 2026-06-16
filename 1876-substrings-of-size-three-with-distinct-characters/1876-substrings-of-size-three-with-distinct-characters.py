class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        def check(string):
            f = {}
            c = 0

            for i in string:
                if i in f:
                    f[i] += 1
                else:
                    f[i] = 1

            for i, j in f.items():
                if j == 1:
                    c += 1
            if c == 3:
                return 1
            return 0
        k = 3
        if len(s) < k:
            return 0
        res = 0
        window = s[:k]
        res += check(window)
        for i in range(k, len(s)):
            window = s[i-k+1:i+1]   # next window of size 3
            res += check(window)

        return res