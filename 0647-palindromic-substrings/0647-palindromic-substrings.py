class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindromeCheck(left,right):
            count=0
            while left>=0 and right<len(s):
                if s[left]!=s[right]:
                    break
                count+=1
                left-=1
                right+=1
            return count
        count=0
        for i in range(len(s)):
            count=count+palindromeCheck(i,i) #odd
            count=count+palindromeCheck(i,i+1) #even
        return count


