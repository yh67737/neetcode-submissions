class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        new=[]
        for i in range(len(gas)):
            new.append(gas[i]-cost[i])
        sumn=0
        start=0
        for i,c in enumerate(new):
            sumn+=c
            if sumn<0:
                start=i+1
                sumn=0
        return start
        