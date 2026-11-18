class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        com=[]
        stack=[]
        for i in range(len(position)):
            com.append([-position[i],speed[i]])
        com.sort()
        for p,s in com:
            hour=(target+p)/s
            if not stack or stack[-1]<hour:
                stack.append(hour)
        return len(stack)





