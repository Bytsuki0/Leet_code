class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = len(nums)
        for j in range(list - 1):
            for i in range(j + 1, list):
                if nums[i] + nums[j] == target:
                    return [i, j]
                