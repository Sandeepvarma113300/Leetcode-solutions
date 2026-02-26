
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        p=sorted(arr, key=lambda x: (x.bit_count(), x))
        return p