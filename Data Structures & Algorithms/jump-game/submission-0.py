class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        goalidx=len(nums)-1
        i=len(nums)-2
        while i>=0:
            if nums[i]>=(goalidx-i):
                goalidx=i
            i-=1
        if goalidx==0:
            return True
        return False


