class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]
        right=[0]
        leftmax,rightmax=0,0
        ans=0
        for i in range(len(height)):
            leftmax=max(leftmax,height[i])
            left.append(leftmax)
            rightmax=max(rightmax,height[len(height)-i-1])
            right.append(rightmax)
        for i in range(len(height)):
            h=min(left[i],right[len(height)-i-1])
            water=max(0,h-height[i])
            ans+=water
        return ans


