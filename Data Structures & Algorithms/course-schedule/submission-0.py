class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            premap[i].append(j)
        visit=set()
        def dfs(i):
            if i in visit:
                return False
            if premap[i]==[]:
                return True
            visit.add(i)
            for j in premap[i]:
                if not dfs(j):
                    return False
            visit.remove(i)
            premap[i]=[]
            return True
        for i in premap:
            if not dfs(i):
                return False
        return True


        