class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap={i:[] for i in range(numCourses)}
        seen=set()
        for i,j in prerequisites:
            hashmap[i].append(j)
        def dfs(i):
            if i in seen:
                return False
            seen.add(i)
            for j in hashmap[i]:
                if not dfs(j):
                    return False
            seen.remove(i)
            hashmap[i]=[]
            return True
        for i in range(numCourses):
            if dfs(i)==False:
                return False
        return True
        