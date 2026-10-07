class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        found = [False] * 3

        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    if not found[i] and triplet[i] == target[i]:
                        found[i] = True
        
        return all(found)
