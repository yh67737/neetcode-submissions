class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            m=(l+r)//2
            c=0
            for i in piles:
                hour=(i+m-1)//m
                c+=hour
            if c>h:
                l=m+1
            else:
                r=m-1
                ans=m
        return ans

