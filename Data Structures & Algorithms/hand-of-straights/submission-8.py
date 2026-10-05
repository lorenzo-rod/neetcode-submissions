from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        counter = defaultdict(int)

        for num in hand:
            counter[num] += 1
        
        for num in range(max(hand) + 1):
            for _ in range(counter[num]):
                for number in range(num, num + groupSize):
                    if not counter[number]:
                        return False
                    counter[number] -= 1
        
        return True
