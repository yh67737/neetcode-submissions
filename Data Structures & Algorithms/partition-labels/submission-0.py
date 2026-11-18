class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count=Counter(s)
        ans=[]
        l=r=0
        letter=set()
        while r<len(s):
            if count[s[r]]>1 and s[r] not in letter:
                letter.add(s[r])
            if s[r] in letter and count[s[r]]==1:
                letter.remove(s[r])
            count[s[r]]-=1
            if not letter:
                ans.append(r-l+1)
                l=r+1
            r+=1
        return ans
            
