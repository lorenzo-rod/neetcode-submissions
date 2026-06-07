class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand_counter = Counter(hand)

        for _ in range(len(hand) // groupSize):
            card = min(hand_counter.keys())
            for _ in range(groupSize):
                if card in hand_counter:
                    hand_counter[card] -= 1
                    if hand_counter[card] == 0:
                        del hand_counter[card]
                    card += 1
                else:
                    return False
        
        return True
