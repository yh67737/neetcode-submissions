class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap={}
        maxans=0
        l,r=0,0
        while r<len(s):
            if s[r] not in hashmap or hashmap[s[r]]<l:
                hashmap[s[r]]=r
            else:
                l=max(hashmap[s[r]]+1,l)
                hashmap[s[r]]=r
            if r-l+1>maxans:
                maxans=r-l+1
            r+=1
        return maxans
            