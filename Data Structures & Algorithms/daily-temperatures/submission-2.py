class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        stack.append((temperatures[0],0))
        for i in range(1,len(temperatures)):
            if temperatures[i]<=stack[-1][0]:
                stack.append((temperatures[i],i))
            else:
                while stack and temperatures[i]>stack[-1][0]:
                    temp,index=stack.pop()
                    ans[index]=i-index
                stack.append((temperatures[i],i))
        return ans