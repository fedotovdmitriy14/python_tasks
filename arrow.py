# Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

# pyramid(0) => [ ]
# pyramid(1) => [ [1] ]
# pyramid(2) => [ [1], [1, 1] ]
# pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
# Note: the subarrays should be filled with 1s

def pyramid(n):
    result_arr = []
    array_of_ones = []
    while n != 0:       
        for i in range(n):
            print(array_of_ones)
            array_of_ones.append(1)
        result_arr.append(array_of_ones)
        n -= 1
        array_of_ones = []        
    return result_arr[::-1]

print(pyramid(3))


def pyramid(n):
    result = []
    for i in range (1, n + 1):
        result.append(i * [1])
    return result