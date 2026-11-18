class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count1=Counter(s1)
        for i in range(0,len(s2)-len(s1)+1):
            count2=Counter(s2[i:len(s1)+i])
            if count1==count2:
                return True
        return False
