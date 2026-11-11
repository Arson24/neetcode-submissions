class Solution:
    def hammingWeight(self, n: int) -> int:
        b = list(bin(n)[2:])
        c=b.count("1")
        return c