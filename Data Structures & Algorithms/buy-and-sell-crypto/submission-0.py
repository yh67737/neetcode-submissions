class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=100
        pro=0
        for i in prices:
            if i<minn:
                minn=i
            if (i-minn)>pro:
                pro=i-minn
        return pro
        