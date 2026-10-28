class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in nums:
            if i in dic:
                return [nums.index(target - i), nums.index(i, 1 + nums.index(target - i))]
            else:
                dic[target - i] = i
