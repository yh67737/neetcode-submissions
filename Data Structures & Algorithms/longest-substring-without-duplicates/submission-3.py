class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        alpha=set()
        i=j=0
        while j<len(s):
            while s[j] in alpha:
                alpha.discard(s[i])
                i+=1
            alpha.add(s[j])
            longest=max(longest,j-i+1)
            j+=1
        return longest