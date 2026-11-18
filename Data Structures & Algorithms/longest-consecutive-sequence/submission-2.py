class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        for i in nums:
            if i-1 in nums:
                continue
            ansc=1
            j=i
            while j+1 in nums:
                ansc+=1
                j=j+1
            if ansc>ans:
                ans=ansc
        return ans