class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]
        leftmax=height[0]
        for i in range(1,len(height)):
            leftmax=max(leftmax,height[i-1])
            left.append(leftmax)
        right=[0]
        rightmax=height[-1]
        for i in range(len(height)-2,-1,-1):
            rightmax=max(rightmax,height[i+1])
            right.append(rightmax)
        ans=0
        for i in range(len(height)):
            h=min(left[i],right[len(height)-1-i])
            water=max(0,h-height[i])
            ans+=water
        return ans


