class TimeMap:

    def __init__(self):
        self.timemap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        listk=self.timemap[key]
        if not listk:
            return ""
        l,r=0,len(listk)-1
        ans=""
        while l<=r:
            m=(l+r)//2
            if listk[m][1]<=timestamp:
                ans=listk[m][0]
                l=m+1
            if listk[m][1]>timestamp:
                r=m-1
        return ans
