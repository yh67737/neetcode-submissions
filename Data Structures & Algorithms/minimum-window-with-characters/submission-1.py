class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t)>len(s):
            return ""
        countt={}
        for i in t:
            if i in countt:
                countt[i]+=1
            else:
                countt[i]=1
        counts={}
        need=len(countt)
        have=0
        left=0
        ans=[-1,-1]
        anslen=float('inf')
        for right in range(len(s)):
            counts[s[right]]=counts.get(s[right],0)+1
            if s[right] in countt and counts[s[right]]==countt[s[right]]:
                have+=1
            while have==need:
                currentlen=right-left+1
                if currentlen<anslen:
                    anslen=currentlen
                    ans=[left,right]
                counts[s[left]]-=1
                if s[left] in countt and counts[s[left]]<countt[s[left]]:
                    have-=1
                left+=1
        if anslen==float('inf'):
            return ""
        else:
            return s[ans[0]:ans[1]+1]






        
            
        