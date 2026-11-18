class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=collections.Counter(nums)
        freq=[[] for _ in range(len(nums)+1)]
        for i in count:
            c=count[i]
            freq[c].append(i)
        ans=[]
        for i in range(len(freq)-1,-1,-1):
            l=freq[i]
            if not l:
                pass
            elif len(l)+len(ans)>k:
                return ans
            else:
                for j in l:
                    ans.append(j)
        return ans



        