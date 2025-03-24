# input: [4, 5, 6, 5, 4, 3, 3, 3, 4]
# output: [3, 3, 3, 4, 4, 4, 5, 5, 6]

from collections import Counter
def sort_by_frequency(arr):
    frequency = Counter(arr)
    sorted_elements = sorted(arr, key=lambda x: (-frequency[x], x))
    
    return sorted_elements

input_list = [4, 5, 6, 5, 4, 4, 4, 3, 3, 3, 4]
output = sort_by_frequency(input_list)
print(output)


