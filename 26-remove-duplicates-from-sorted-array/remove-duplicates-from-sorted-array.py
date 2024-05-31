class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = nums 
        for m in range(len(n)):
            for i in range(len(n)-1):
                if n[i] == n[i+1]:
                    n.pop(i+1)
                    break
        
        
        return len(n)