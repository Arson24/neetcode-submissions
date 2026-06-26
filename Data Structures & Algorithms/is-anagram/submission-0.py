class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=dict(Counter(s))
        l2=dict(Counter(t))
        if l1==l2:
            return True
        else:
            return False
        return