class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        i=0
        count=dict()
        maxfreq=0
        for j in range(len(s)):
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]]=1
            maxfreq=max(maxfreq,count[s[j]])
            while (j-i+1-maxfreq)>k:
                count[s[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans

        