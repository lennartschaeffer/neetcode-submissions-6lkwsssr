class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """sort the list in ascending order
        [1,2,3,6,2,3,4,7,8]
        [1,2,2,3,3,4,6,7,8]
        """
        counts = {}
        for h in hand:
            counts[h] = counts.get(h,0) + 1
        
        hand.sort()

        for i in range(len(hand)):
            valid = 0
            currentVal = hand[i]
            if currentVal not in counts:
                continue
            for j in range(groupSize):
                if currentVal not in counts:
                    return False
                counts[currentVal] -= 1
                if counts[currentVal] == 0:
                    del counts[currentVal]
                currentVal += 1
            if not counts:
                return True
        
        return True



         