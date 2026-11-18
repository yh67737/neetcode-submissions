class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=''
        for i in strs:
            ans+=str(len(i))
            ans+='#'
            ans+=str(i)
        return ans


    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            ans.append(str(s[i:j]))
            i=j
        return ans