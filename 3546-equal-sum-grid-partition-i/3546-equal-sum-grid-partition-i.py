class Solution(object):
    def canPartitionGrid(self, grid):
        total = sum(sum(row) for row in grid)
        
        if total % 2 != 0:
            return False
        
        curr = 0
        for i in range(len(grid) - 1):
            curr += sum(grid[i])
            if curr == total - curr:
                return True

        curr = 0
        cols = len(grid[0])
        
        for j in range(cols - 1):
            for i in range(len(grid)):
                curr += grid[i][j]
            
            if curr == total - curr:
                return True
        
        return False