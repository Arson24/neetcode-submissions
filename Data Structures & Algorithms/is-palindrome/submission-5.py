class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1 = []
        for i in s.lower(): 
            ascii_val = ord(i)
            if (48 <= ascii_val <= 57) or (97 <= ascii_val <= 122):
                l1.append(i)
        cleaned_str = "".join(l1)
        return cleaned_str == cleaned_str[::-1]