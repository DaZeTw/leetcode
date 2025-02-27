class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        l,ans = 0,0
        for r in range(len(s)):
            if s[r] not in temp:
                temp.add(s[r])
                ans = max(ans,r-l+1)
            else:
                while s[r] in temp:
                    temp.remove(s[l])
                    l +=1
                temp.add(s[r])
        return ans