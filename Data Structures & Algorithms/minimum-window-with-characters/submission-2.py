class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        hasht={}
        for i in t:
            if i not in hasht:
                hasht[i]=1
            else:
                hasht[i]+=1
        j=0
        hashs={}
        have,need=0,len(hasht)
        ans=[-1,-1]
        anslen=float("infinity")
        for i in range(len(s)):
            if s[i] not in hashs:
                hashs[s[i]]=1
            else:
                hashs[s[i]]+=1
            if s[i] in hasht and hashs[s[i]]==hasht[s[i]]:
                have+=1
            while have==need:
                if i-j+1<anslen:
                    ans=[j,i]
                    anslen=i-j+1
                hashs[s[j]]-=1
                if s[j] in hasht and hashs[s[j]]<hasht[s[j]]:
                    have-=1
                j+=1
        l,r=ans
        if anslen!=float("infinity"):
            return s[l:r+1]
        else:
            return ""



        
