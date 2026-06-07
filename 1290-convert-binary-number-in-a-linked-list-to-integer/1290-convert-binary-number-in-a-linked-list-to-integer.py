# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp=head
        b=[]
        while temp:
            b.append(str(temp.val))
            temp=temp.next
        s="".join(b)
        return int(s,2)
