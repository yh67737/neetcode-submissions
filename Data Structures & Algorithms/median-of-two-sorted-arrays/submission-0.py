class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index=math.ceil((len(nums1)+len(nums2)+1)/2.0)
        p1,p2=0,0
        left,right=0,0
        count=0
        while count<index:
            left=right
            if p1>=len(nums1) or (p2<len(nums2) and nums1[p1]>nums2[p2]):
                right=nums2[p2]
                p2+=1
            else:
                right=nums1[p1]
                p1+=1
            count+=1
        if (len(nums1)+len(nums2))%2==0:
            return float(left+right)/2.0
        else:
            return float(right)