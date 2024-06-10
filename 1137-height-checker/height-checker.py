class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ls = sorted(heights)
        out = 0
        for i in range(len(ls)):        
            if heights[i] != ls[i]:
                out += 1
        return out