class Solution:
    def isHappy(self, n: int) -> bool:
        seen_number = []

        n_str = str(n)
        number = sum([int(digit)**2 for digit in n_str])
        
        
        while number not in seen_number:
            seen_number.append(number)
            n_str = str(number)
            number = sum([int(digit)**2 for digit in n_str])
        
        if number == 1:
            return True
        else:
            return False
        