class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store=[0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            store[i]=min(store[i-1]+cost[i-1],store[i-2]+cost[i-2])
        return store[len(cost)]
