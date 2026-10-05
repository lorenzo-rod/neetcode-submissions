class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        hand.sort()
        counter = [0] * (hand[-1] + 1)

        for num in hand:
            counter[num] += 1
        
        for num in range(len(counter)):
            for _ in range(counter[num]):
                for number in range(num, num + groupSize):
                    if number > hand[-1] or not counter[number]:
                        return False
                    counter[number] -= 1
        
        return True
