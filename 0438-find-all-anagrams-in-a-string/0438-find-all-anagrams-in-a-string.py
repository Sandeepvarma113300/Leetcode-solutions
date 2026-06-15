from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        k = len(p)
        b = []

        freq = {}
        for i in p:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        window = s[:k]
        freq1 = {}

        for i in window:
            if i in freq1:
                freq1[i] += 1
            else:
                freq1[i] = 1

        if freq == freq1:
            b.append(0)

        for i in range(k, len(s)):
            left = s[i - k]

            freq1[left] -= 1
            if freq1[left] == 0:
                del freq1[left]

            if s[i] in freq1:
                freq1[s[i]] += 1
            else:
                freq1[s[i]] = 1

            if freq1 == freq:
                b.append(i - k + 1)

        return b