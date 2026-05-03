class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen = []

        for num in nums:
            if num in has_seen:
                return True
            else:
                has_seen.append(num)

        return False
        