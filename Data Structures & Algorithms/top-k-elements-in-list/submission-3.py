class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=collections.Counter(nums)
        ans=[]
        lis=[[] for _ in range(len(nums)+1)]
        for i in count:
            c=count[i]
            lis[c].append(i)
        flag=0
        for i in range(len(nums),-1,-1):
            if lis[i] and flag<k:
                for j in lis[i]:
                    ans.append(j)
                    flag+=1
        return ans


