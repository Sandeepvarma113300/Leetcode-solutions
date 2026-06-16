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
    """
    class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        freq = {}
        k = 3
        res = 0

        for i in s[:k]:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        if len(freq) == 3:
            res += 1

        for i in range(k, len(s)):
            left = s[i-k]

            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]

            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

            if len(freq) == 3:
                res += 1

        return res"""