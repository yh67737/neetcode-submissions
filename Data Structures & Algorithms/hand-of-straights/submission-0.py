class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize!=0:
            return False
        hand.sort()
        count=Counter(hand)
        for i in hand:
            if count[i]>0:
                for j in range(i,i+groupSize):
                    if count[j]<=0:
                        return False
                    count[j]-=1
        return True
        

        
        