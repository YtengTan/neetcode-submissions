class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones.sort()

        while len(stones) > 1:
            
            largest_two_stone_smashed = stones[-1] - stones[-2]
            
            stones = stones[:-2]
            stones.append(largest_two_stone_smashed)
            stones.sort()
        
        return stones[0]
        