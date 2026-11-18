class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap=dict()
        for i in range(len(nums)):
            res=target-nums[i]
            if res in hashmap:
                return [hashmap[res],i]
            else:
                hashmap[nums[i]]=i
        return []