class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = False 
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ' and temp:
                break
            if s[i] != ' ':
                temp = True
                count += 1
        return count
        