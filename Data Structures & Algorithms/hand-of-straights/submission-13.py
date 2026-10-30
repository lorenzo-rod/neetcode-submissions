from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        counter = defaultdict(int)

        for num in hand:
            counter[num] += 1
        
        for num in hand:
            start = num
            while counter[start - 1]:
                start -= 1
            while start <= num:
                while counter[start]:
                    for number in range(start, start + groupSize):
                        if not counter[number]:
                            return False
                        counter[number] -= 1
                start += 1

        return True
