class Solution:
    def partitionString(self, s: str) -> int:
        if (s==""):
            return 0
        seen = set(s)
        res = 0
        for ch in s:
            if ch not in seen:
                seen.add(ch)
            else:
                seen.clear()
                seen.add(ch)
                res +=1
        return res