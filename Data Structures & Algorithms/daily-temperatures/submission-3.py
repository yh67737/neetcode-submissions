class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        stack.append((temperatures[0],0))

        for i in range(1,len(temperatures)):
            if temperatures[i]<=stack[-1][0]:
                stack.append((temperatures[i],i))
            else:
                while stack and temperatures[i]>stack[-1][0]:
                    num,idx=stack.pop()
                    ans[idx]=i-idx
                stack.append((temperatures[i],i))
        return ans
        