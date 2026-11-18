class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        for i in range(len(intervals)):
            s,e=intervals[i]
            if not ans or s>ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(ans[-1][1],e)
        return ans
                
