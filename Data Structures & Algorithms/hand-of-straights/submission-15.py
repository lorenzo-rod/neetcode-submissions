from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        counter = defaultdict(int)

        for num in hand:
            counter[num] += 1

        for num in hand:
            if counter[num]:
                for number in range(num, num + groupSize):
                    if not counter[number]:
                        return False
                    counter[number] -= 1
        
        return True
