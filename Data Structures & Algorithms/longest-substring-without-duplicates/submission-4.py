class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        hashmap=dict()
        i=j=0
        while j<len(s):
            if s[j] not in hashmap or hashmap[s[j]]<i:
                hashmap[s[j]]=j
                if j-i+1>ans:
                    ans=j-i+1
            else:
                i=hashmap[s[j]]+1
                hashmap[s[j]]=j
            j+=1
        return ans