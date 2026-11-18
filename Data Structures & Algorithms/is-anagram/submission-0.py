class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1=dict()
        hash2=dict()
        if len(s)!=len(t):
            return False
        j=0
        for i in range(len(s)):
            if s[i] in hash1:
                hash1[s[i]]+=1
            else:
                hash1[s[i]]=1
            if t[j] in hash2:
                hash2[t[j]]+=1
            else:
                hash2[t[j]]=1
            j+=1
        if hash1==hash2:
            return True
        return False




