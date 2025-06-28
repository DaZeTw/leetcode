class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        temp = [[0]*n for _ in range(m)]

        for x,y in guards:
            temp[x][y] = 2
        for x,y in walls:
            temp[x][y] = 2
        
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        for cx,cy in guards:
            for dx,dy in directions:
                x, y = cx,cy
                while 0<=x+dx<m and 0<=y+dy<n and temp[x+dx][y+dy]!=2:
                    x += dx
                    y += dy
                    temp[x][y]=1
        
        return sum(row.count(0) for row in temp)