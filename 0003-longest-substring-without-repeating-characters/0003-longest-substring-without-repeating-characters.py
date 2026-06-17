class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        max_len=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left=left+1
            seen.add(s[i])
            curr_len=i-left+1
            max_len=max(curr_len,max_len)
        return max_len