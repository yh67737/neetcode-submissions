class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]
        rightmax=[0]
        ans=0
        for i in range(len(height)-1):
            if height[i]>leftmax[-1]:
                leftmax.append(height[i])
            else:
                leftmax.append(leftmax[-1])
            if height[len(height)-i-1]>rightmax[-1]:
                rightmax.append(height[len(height)-i-1])
            else:
                rightmax.append(rightmax[-1])
        for i in range(len(height)):
            w=min(leftmax[i],rightmax[len(height)-i-1])-height[i]
            ans+=max(0,w)
        return ans
