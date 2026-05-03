class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_digit_square(number: int):
            n = number
            summation = 0
            while n > 0:
                summation += (n % 10)**2
                n //= 10
            return summation
        
        seen_number = []

        # n_str = str(n)
        # number = sum([int(digit)**2 for digit in n_str])
        number = sum_digit_square(n)
        
        
        while number not in seen_number:
            seen_number.append(number)
            # n_str = str(number)
            # number = sum([int(digit)**2 for digit in n_str])
            number = sum_digit_square(number)
        
        if number == 1:
            return True
        else:
            return False
        