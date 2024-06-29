class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x = -1
        for i in range (len(nums)):
            if nums[i] == target or nums[i] > target:
                x = i
                break

        if x == -1:
            x = len(nums)
            return x
        else:
            return x
