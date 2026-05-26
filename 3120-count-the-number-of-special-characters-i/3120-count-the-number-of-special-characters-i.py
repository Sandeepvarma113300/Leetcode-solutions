
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l=set()
        u=set()
        for i in word:
            if i.islower():
                l.add(i)
            else:
                u.add(i.lower())
        return len(l&u)