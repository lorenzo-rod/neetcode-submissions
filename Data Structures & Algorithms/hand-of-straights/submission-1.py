from sortedcontainers import SortedDict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand_counter = SortedDict(Counter(hand))

        for _ in range(n // groupSize):
            card = hand_counter.peekitem(0)[0]
            for _ in range(groupSize):
                if card in hand_counter:
                    hand_counter[card] -= 1
                    if hand_counter[card] == 0:
                        del hand_counter[card]
                    card += 1
                else:
                    return False
        
        return True
