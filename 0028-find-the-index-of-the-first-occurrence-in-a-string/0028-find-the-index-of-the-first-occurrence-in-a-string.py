class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle)>len(haystack)):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j = 0
                while j<len(needle) and i+j<len(haystack):
                    if haystack[i+j] != needle[j]:
                        break
                    j +=1
                if (j == len(needle)):
                    return i
        return -1 
        