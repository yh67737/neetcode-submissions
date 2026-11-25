from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        tcount=Counter(t)
        scount={}
        need=len(tcount)
        have=0
        l=0
        ans=[-1,-1]
        anslen=float("inf")
        for r,i in enumerate(s):
            if i in scount:
                scount[i]+=1
            else:
                scount[i]=1
            if i in tcount and scount[i]==tcount[i]:
                have+=1
            while have==need:
                scount[s[l]]-=1
                if s[l] in tcount and tcount[s[l]]>scount[s[l]]:
                    have-=1
                if r-l+1<anslen:
                    ans=[l,r]
                    anslen=r-l+1
                l+=1
        return s[ans[0]:ans[1]+1]


                