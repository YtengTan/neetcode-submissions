class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []

        squares = {
            '0': 0, '1': 1, '2': 4, '3': 9, '4': 16,
            '5': 25, '6': 36, '7': 49, '8': 64, '9': 81
        }

        while n not in seen:
            if n == 1:
                return True

            seen.append(n)
            n = sum([squares[d] for d in str(n)])

        return False