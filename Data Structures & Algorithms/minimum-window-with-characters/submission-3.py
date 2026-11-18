class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hasht={}
        hashs={}
        for i in t:
            if i not in hasht:
                hasht[i]=1
            else:
                hasht[i]+=1
        need=len(hasht)
        have=0
        l=0
        ans=[-1,-1]
        anslen=float("infinity")
        for r in range(len(s)):
            if s[r] not in hashs:
                hashs[s[r]]=1
            else:
                hashs[s[r]]+=1
            if s[r] in hasht and hasht[s[r]]==hashs[s[r]]:
                have+=1
            while have==need:
                hashs[s[l]]-=1
                if s[l] in hasht and hasht[s[l]]>hashs[s[l]]:
                    have-=1
                if r-l+1<anslen:
                    ans=[l,r]
                    anslen=r-l+1
                l+=1
        l,r=ans
        if anslen==float("infinity"):
            return ""
        else:
            return s[l:r+1]
