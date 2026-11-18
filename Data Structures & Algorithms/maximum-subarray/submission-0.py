class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float("-inf")
        cur=0
        for i in nums:
            cur=max(cur+i,i)
            ans=max(cur,ans)
        return ans