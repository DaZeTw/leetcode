class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [c.lower() for c in s if c.isalnum()]
        
        # Check if the filtered characters form a palindrome
        return filtered_chars == filtered_chars[::-1]