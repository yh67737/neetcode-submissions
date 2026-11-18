class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        hashmap = {c: [] for word in words for c in word}
        ans=[]

        def insert(x,y):
            if x not in hashmap:
                hashmap[x]=[]
            hashmap[x].append(y)

        for i in range(len(words)-1):
            a,b=words[i],words[i+1]
            if len(a)>len(b) and a.startswith(b):
                return ""
            j=0
            while j<min(len(a),len(b)):
                if a[j]!=b[j]:
                    insert(a[j],b[j])
                    break
                j+=1
        
        seen=set()
        complete=set()
        
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
            ans.append(i)
            return True
        
        for i in hashmap:
            if dfs(i)==False:
                return ""
        return "".join(ans[::-1])
        



                



