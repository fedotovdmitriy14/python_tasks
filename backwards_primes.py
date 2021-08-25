# Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a different prime. (This rules out primes which are palindromes.)

# Examples:
# 13 17 31 37 71 73 are Backwards Read Primes
# 13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.

# Task
# Find all Backwards Read Primes between two positive given numbers (both inclusive), the second one always being greater than or equal to the first one. The resulting array or the resulting string will be ordered following the natural order of the prime numbers.

# Examples (in general form):
# backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967] backwardsPrime(501, 599) => []

# See "Sample Tests" for your language.



def backwards_prime(start, stop):
    result = []
    for number in range(start, stop+1):
        counter = 0
        if len(str(number)) != 1:
            for i in range(2, number):
                if number % i == 0:
                    counter += 1
                    break
            if counter == 0:
                number = int(str(number)[::-1])
                for i in range(2, number):
                    if number % i == 0:
                        counter += 1
                        break
            if counter == 0 and number != int(str(number)[::-1]):
                result.append(int(str(number)[::-1]))
    return result

print(backwards_prime(2, 100)) 
print(backwards_prime(7000, 7100))

# => [13, 17, 31, 37, 71, 73, 79, 97]


#optimized version 

import math


def backwards_prime(start, stop):
    result = []
    for number in range(start, stop+1):
        reverse_number = int(str(number)[::-1])
        counter = 0
        if len(str(number)) != 1 and number != reverse_number:
            max_div = math.floor(math.sqrt(number))                                     #сокращаем делители вдвое 
            for i in range(2, 1 + max_div):
                if number % i == 0:
                    counter += 1
                    break
            if counter == 0:
                number = reverse_number
                max_div = math.floor(math.sqrt(number))
                for i in range(2, 1 + max_div):
                    if number % i == 0:
                        counter += 1
                        break
            if counter == 0:
                result.append(int(str(number)[::-1]))
    return result

print(backwards_prime(2, 100)) 
print(backwards_prime(7000, 7100))