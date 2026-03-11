class Solution:
    def findComplement(self, num: int) -> int:
        m=(1<<num.bit_length())-1
        return num^m