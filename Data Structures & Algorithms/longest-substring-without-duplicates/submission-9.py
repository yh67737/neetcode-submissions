class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hashmap={}
        i,j=0,0
        ans=0
        while i<len(s) and j<len(s):
            if s[j] not in hashmap or hashmap[s[j]]<i:
                hashmap[s[j]]=j
                ans=max(ans,j-i+1)
            else:
                i=max(i,hashmap[s[j]]+1)
                hashmap[s[j]]=j
            j+=1
        return ans
                
            
            
