class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            hashmap[i].append(j)
        seen=set()
        finish=set()
        ans=[]
        def dfs(i):
            if i in seen:
                return False
            if i in finish:
                return True
            seen.add(i)
            for j in hashmap[i]:
                if not dfs(j):
                    return False
            seen.remove(i)
            finish.add(i)
            ans.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans

        