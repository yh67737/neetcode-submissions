class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            hashmap[i].append(j)
        seen=set()
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
            if not dfs(i):
                return False
        return True

        