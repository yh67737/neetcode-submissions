class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            premap[i].append(j)
        visit=set()#store fully processed nodes
        cycle=set()#store seen nodes in one dfs
        ans=[]
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            for j in premap[i]:
                if not dfs(j):
                    return False
            cycle.remove(i)
            visit.add(i)
            ans.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans

        