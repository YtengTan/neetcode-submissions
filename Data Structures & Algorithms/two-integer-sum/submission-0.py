class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_nums = len(nums)
        results = []
        for i in range(n_nums):
            num_i = nums[i]
            for j in range(i+1,n_nums):
                num_j = nums[j]

                if num_i + num_j == target:
                    return [i,j]

        return None
        