class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            cur = nums[i]
            if (target - cur) in d:
                return [i, d[target - cur]]
            d[cur] = i

