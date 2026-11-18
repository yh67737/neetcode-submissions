class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap={i:[] for i in range(numCourses)}
        complete=set()
        seen=set()
        ans=[]
        for i,j in prerequisites:
            hashmap[i].append(j)
        def dfs(i):
            if i in seen:
                return False
            if i in complete:
                return True
            seen.add(i)
            for j in hashmap[i]:
                if not dfs(j):
                    return False
            seen.remove(i)
            complete.add(i)
            hashmap[i]=[]
            ans.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans

        