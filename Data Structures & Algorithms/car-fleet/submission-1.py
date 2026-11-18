class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        com=[]
        for i in range(len(position)):
            com.append((-position[i],speed[i]))
        com.sort()
        stack=[]
        for i in range(len(com)):
            pos,spe=com[i]
            hour=(target+pos)/spe
            if not stack or hour>stack[-1]:
                stack.append(hour)
        return len(stack)

