class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        while start<=end:
            mid = (start+end)//2
            total_hours = sum(math.ceil(pile/mid) for pile in piles)
            if total_hours>h:
                start = mid+1
            else:
                end = mid-1
        return start
        
        