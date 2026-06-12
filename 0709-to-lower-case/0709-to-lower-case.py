class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=""
        for i in s:
            if i.isupper():
                ans=ans+i.lower()
            else:
                ans=ans+i
        return ans