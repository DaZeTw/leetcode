class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        rStart = 0
        rEnd = n-1
        while rStart <= rEnd:
            rMid = (rStart+rEnd)//2
            tempStart = matrix[rMid][0]
            tempEnd = matrix[rMid][m-1]
            if (tempEnd<target):
                rStart = rMid+1
            elif (tempStart>target):
                rEnd = rMid-1
            else:
                cStart = 0 
                cEnd = m-1
                while cStart <= cEnd:
                    cMid = (cStart+cEnd)//2
                    val = matrix[rMid][cMid]
                    if (val==target): return True
                    if (val<target):
                        cStart = cMid +1
                    else:
                        cEnd = cMid -1
                break
        return False
        