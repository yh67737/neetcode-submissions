class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        new=[]
        for i in triplets:
            if i[0]<=target[0] and i[1]<=target[1] and i[2]<=target[2]:
                new.append(i)
        flag=[0,0,0]
        for i in new:
            if i[0]==target[0]:
                flag[0]=1
            if i[1]==target[1]:
                flag[1]=1
            if i[2]==target[2]:
                flag[2]=1
        if flag==[1,1,1]:
            return True
        return False

        