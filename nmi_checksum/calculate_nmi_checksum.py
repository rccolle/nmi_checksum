import math

def round_up_to_nearest_ten(x):
    return int(math.ceil(x / 10.0)) * 10

def sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def calculate_nmi_checksum(nmi):
    nmi_as_list = [digit for digit in nmi]
    
    sum_of_even_index_digits = sum([sum_of_digits(ord(digit) * 2) for digit in nmi_as_list[1::2]])
    
    sum_of_odd_index_digits = sum([sum_of_digits(ord(digit)) for digit in nmi_as_list[::2]])
    
    sum_both_sums = sum_of_even_index_digits + sum_of_odd_index_digits
    
    next_highest_tens = round_up_to_nearest_ten(sum_both_sums)
    
    return (next_highest_tens - sum_both_sums) % 10
