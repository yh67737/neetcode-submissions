class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            res=-nums[i]
            while j<k:
                if nums[j]+nums[k]==res:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j+1]==nums[j]:
                        j+=1
                    while j<k and nums[k-1]==nums[k]:
                        k-=1
                    j+=1
                while j<k and nums[j]+nums[k]>res:
                    k-=1
                while j<k and nums[j]+nums[k]<res:
                    j+=1
                
        return list(ans)

