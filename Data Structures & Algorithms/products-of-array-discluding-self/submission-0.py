class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        pro=1
        prol=1
        ans=[]
        for i in range(len(nums)):
            pro=pro*nums[i]
            left.append(pro)
            prol=prol*nums[len(nums)-i-1]
            right.append(prol)
        for i in range(len(nums)):
            ans.append(left[i]*right[len(nums)-i-1])
        return ans


