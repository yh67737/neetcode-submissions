class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        i=j=0
        dicalpha=dict()
        while j<len(s):
            if s[j] not in dicalpha or dicalpha[s[j]] < i:
                dicalpha[s[j]]=j
                if (j-i+1)>longest:
                    longest=j-i+1
            else:
                i=dicalpha[s[j]]+1
                dicalpha[s[j]]=j
            j+=1
        return longest

