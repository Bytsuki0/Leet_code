class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        n, m = len(grid), len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)
        
        size = len(arr)

        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD

        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
  
        result = [(prefix[i] * suffix[i]) % MOD for i in range(size)]
 
        res = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(result[idx])
                idx += 1
            res.append(row)
        
        return res