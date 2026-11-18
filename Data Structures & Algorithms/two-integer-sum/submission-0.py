class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            t=target-nums[i]
            if t in hash:
                return [hash[t],i]
            hash[nums[i]]=i
        return []
        