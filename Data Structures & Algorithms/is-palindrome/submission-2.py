class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only lowercase letters and numbers
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        
        # Check if it reads the same forward and backward
        return cleaned == cleaned[::-1]

