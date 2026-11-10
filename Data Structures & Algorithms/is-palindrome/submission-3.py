class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1 = []
        for i in s.lower(): # Convert to lower up front
            ascii_val = ord(i)
            # Use 'or' because a character can only belong to one range
            if (48 <= ascii_val <= 57) or (97 <= ascii_val <= 122):
                l1.append(i)
                
        # Turn the list back into a string to compare it with its reverse
        cleaned_str = "".join(l1)
        return cleaned_str == cleaned_str[::-1]