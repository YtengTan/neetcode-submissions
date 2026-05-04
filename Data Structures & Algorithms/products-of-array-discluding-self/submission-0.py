class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod_without_i(nums, index_i):
            prod = 1
            # prod = num*prod if i!=index_i else 1*prod for (i,num) in enumerate(nums)
            for (i,num) in enumerate(nums):
                if i==index_i:
                    continue
                prod = num*prod
            return prod


        
        results = []
        n_nums = len(nums)
        
        if 0 in nums:
            index_of_0 = nums.index(0)
            results = [0] * n_nums
            results[index_of_0] = prod_without_i(nums, index_of_0)
            return results

        for i in range(n_nums):
            results.append(prod_without_i(nums,i))
        
        return results