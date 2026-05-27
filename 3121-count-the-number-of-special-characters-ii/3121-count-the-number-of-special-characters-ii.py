class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i.lower() in word and i.upper() in word:
                last_lower=word.rfind(i)
                first_upper=word.find(i.upper())
                if last_lower < first_upper:
                    c=c+1
        return c