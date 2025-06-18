class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cookTime = 0
        sumTime = 0
        for cus in customers:
            waitingTime = max(0, cookTime-cus[0]) + cus[1]
            cookTime = cus[0] + waitingTime
            sumTime += waitingTime
        return float(sumTime)/len(customers)
        