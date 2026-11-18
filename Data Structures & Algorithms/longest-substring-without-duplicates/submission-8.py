class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxa=0
        i=j=0
        hashmap={}
        while i<len(s) and j<len(s):
            if s[j] not in hashmap or hashmap[s[j]]<i:
                hashmap[s[j]]=j
                ans=j-i+1
                maxa=max(ans,maxa)
            else:
                i=max(hashmap[s[j]]+1,i)
                hashmap[s[j]]=j
            j+=1
        return maxa

            



