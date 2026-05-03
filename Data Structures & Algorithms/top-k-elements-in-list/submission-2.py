class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_digit = []
        seen_digit_freq = []

        for num in nums:
            if num not in seen_digit:
                seen_digit.append(num)
                seen_digit_freq.append(1)
            else:
                digit_idx = seen_digit.index(num)
                seen_digit_freq[digit_idx] += 1

        sorted_with_idx = sorted(enumerate(seen_digit_freq), key=lambda x: x[1])
        results = []
        for i in range(k):
            digit_idx = sorted_with_idx[-1-i][0]
            results.append(seen_digit[digit_idx])
        # n_unique_digit = len(seen_digit_freq)
        # results = []
        # for i in range(n_unique_digit):
        #     if seen_digit_freq[i] >= k:
        #         results.append(seen_digit[i])
        
        return results
