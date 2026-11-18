class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minans=1
        maxans=max(piles)
        ans=maxans
        while minans<=maxans:
            mid=(minans+maxans)//2
            hour=0
            for i in piles:
                hour+=math.ceil(float(i) / mid)
            if hour<=h:
                ans=mid
                maxans=mid-1
            else:
                minans=mid+1
        return ans


