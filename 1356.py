def sortByBits(arr):
    def count_ones(num):
        return bin(num).count('1')

    return sorted(arr, key=lambda x: (count_ones(x), x))

# Example usage:
input_array = [0,1,2,3,4,5,6,7,8]
result = sortByBits(input_array)
print(result)

# [0,1,2,4,8,3,5,6,7]