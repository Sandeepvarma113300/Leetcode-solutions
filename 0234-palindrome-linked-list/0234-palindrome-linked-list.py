# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        b=[]
        temp=head
        while temp:
            b.append(int(temp.val))
            temp=temp.next
        return b==b[::-1]
